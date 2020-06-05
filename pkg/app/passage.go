// Brief: Bible Passage handling
// Primary responsibility: Parsing of Bible Passages from HTML

package app

import (
	"fmt"
	"log"
	"strings"

	"golang.org/x/net/html"

	bmul "github.com/julwrites/BotMultiplexer"
	"github.com/julwrites/ScriptureBot/pkg/api"
)

func GetReference(doc *html.Node, env *bmul.SessionData) string {
	refNode, err := api.FindByClass(doc, "bcv")
	if err != nil {
		log.Printf("Error parsing for reference: %v", err)
		return ""
	}

	return refNode.FirstChild.Data
}

func ParseNodesForPassage(node *html.Node) string {
	var text string
	var parts []string

	for child := node.FirstChild; child != nil; child = child.NextSibling {
		parts = append(parts, text)

		switch tag := child.Data; tag {
		case "span":
			childText := strings.Trim(ParseNodesForPassage(child), " ")
			if len(childText) > 0 {
				parts = append(parts, childText)
			}
		case "sup":
			isFootnote := func(node *html.Node) bool {
				for _, attr := range node.Attr {
					if attr.Key == "class" && attr.Val == "footnote" {
						return true
					}
				}
				return false
			}
			if isFootnote(child) {
				break
			}
			childText := strings.Trim(ParseNodesForPassage(child), " ")
			if len(childText) > 0 {
				parts = append(parts, fmt.Sprintf("^%s^", childText))
			}
			break
		default:
			parts = append(parts, child.Data)
		}
	}

	text = strings.Join(parts, "")

	if node.Data == "h1" || node.Data == "h2" || node.Data == "h3" {
		text = fmt.Sprintf("*%s*", text)
	}
	return text
}

func GetPassage(doc *html.Node, env *bmul.SessionData) string {
	passageNode, startErr := api.FindByClass(doc, fmt.Sprintf("version-%s result-text-style-normal text-html", api.DeserializeUserConfig(env.User.Config).Version))
	if startErr != nil {
		log.Printf("Error parsing for passage: %v", startErr)
		return ""
	}

	filtNodes := api.FilterChildren(passageNode, func(child *html.Node) bool {
		switch tag := child.Data; tag {
		case "h1":
			fallthrough
		case "h2":
			fallthrough
		case "h3":
			fallthrough
		case "p":
			return true
		}
		return false
	})

	textBlocks := api.MapNodeList(filtNodes, ParseNodesForPassage)

	var passage strings.Builder

	for _, block := range textBlocks {
		passage.WriteString(block)
		passage.WriteString("\n")
	}

	return passage.String()
}

func GetBiblePassage(env bmul.SessionData) bmul.SessionData {
	if len(env.Msg.Message) > 0 {

		doc := api.QueryBiblePassage(env.Msg.Message, api.DeserializeUserConfig(env.User.Config).Version)

		ref := GetReference(doc, &env)
		log.Printf("Reference retrieved: %s", ref)

		if len(ref) > 0 {
			log.Printf("Getting passage")
			env.Res.Message = GetPassage(doc, &env)
		}
	}

	return env
}