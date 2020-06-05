package test

import (
	"testing"

	"github.com/julwrites/ScriptureBot/pkg/api"
	"golang.org/x/net/html"
)

// HTML tests
type HtmlTestStruct struct {
	Root *html.Node
	List []*html.Node
}

func GetTestData() HtmlTestStruct {
	var attr html.Attribute
	attr.Key = "class"
	attr.Val = "positive"

	var test1 html.Node
	test1.Type = html.ElementNode
	test1.Data = "positive"
	test1.Attr = append(test1.Attr, attr)

	var test2 html.Node
	test2.Type = html.CommentNode
	test2.Data = "positive"

	var test3 html.Node
	test3.Type = html.ElementNode
	test3.Data = "positive"
	test3.Attr = append(test3.Attr, attr)

	test2.AppendChild(&test3)

	var root html.Node
	root.AppendChild(&test1)
	root.AppendChild(&test2)

	var list []*html.Node
	list = append(list, &test1)
	list = append(list, &test2)
	list = append(list, &test3)

	return HtmlTestStruct{Root: &root, List: list}
}

func TestGetHtml(t *testing.T) {
	pos := api.GetHtml("https://www.google.com")

	if pos == nil {
		t.Errorf("Failed GetHtml positive scenario")
	}

	neg := api.GetHtml("https://www.google.thiscannotbe")

	if neg != nil {
		t.Errorf("Failed GetHtml negative scenario")
	}
}

func TestFindNode(t *testing.T) {
	root := GetTestData().Root

	pos := api.FindNode(root, func(node *html.Node) bool { return node.Data == "positive" })

	if pos == nil {
		t.Errorf("Failed FindNode positive scenario")
	}

	neg := api.FindNode(root, func(node *html.Node) bool { return node.Data == "negative" })

	if neg != nil {
		t.Errorf("Failed FindNode negative scenario")
	}
}

func TestFilterTree(t *testing.T) {
	root := GetTestData().Root

	pos := api.FilterTree(root, func(node *html.Node) bool { return node.Data == "positive" })

	if len(pos) != 3 {
		t.Errorf("Failed TestFilterTree positive scenario")
	}

	neg := api.FilterTree(root, func(node *html.Node) bool { return node.Data == "negative" })

	if len(neg) != 0 {
		t.Errorf("Failed TestFilterTree negative scenario")
	}
}

func TestFilterNodeList(t *testing.T) {
	list := GetTestData().List

	pos := api.FilterNodeList(list, func(node *html.Node) bool { return node.Data == "positive" })

	if len(pos) != 3 {
		t.Errorf("Failed FilterNodeList positive scenario")
	}

	neg := api.FilterNodeList(list, func(node *html.Node) bool { return node.Data == "negative" })

	if len(neg) != 0 {
		t.Errorf("Failed FilterNodeList negative scenario")
	}
}

func TestFilterChildren(t *testing.T) {
	root := GetTestData().Root

	pos := api.FilterChildren(root, func(node *html.Node) bool { return node.Data == "positive" })

	if len(pos) != 2 {
		t.Errorf("Failed FilterChildren positive scenario")
	}

	neg := api.FilterChildren(root, func(node *html.Node) bool { return node.Data == "negative" })

	if len(neg) != 0 {
		t.Errorf("Failed FilterChildren negative scenario")
	}
}

func TestMapTree(t *testing.T) {
	root := GetTestData().Root

	output := api.MapTree(root, func(node *html.Node) string { return node.Data })
	if len(output) != 4 {
		t.Errorf("Failed MapTree")
	}
}

func TestMapNodeList(t *testing.T) {
	list := GetTestData().List

	output := api.MapNodeList(list, func(node *html.Node) string { return node.Data })

	if len(output) != 3 {
		t.Errorf("Failed MapNodeList positive scenario")
	}
}

func TestFindByClass(t *testing.T) {
	root := GetTestData().Root

	pos, perror := api.FindByClass(root, "positive")

	if pos == nil || perror != nil {
		t.Errorf("Failed FindByClass positive scenario")
	}

	neg, nerror := api.FindByClass(root, "negative")

	if neg != nil || nerror == nil {
		t.Errorf("Failed FindByClass negative scenario")
	}
}

func TestFilterByNodeType(t *testing.T) {
	root := GetTestData().Root

	output := api.FilterByNodeType(root, html.ElementNode)

	if len(output) != 2 {
		t.Errorf("Failed FilterByNodeType")
	}
}

// URL Query tests
func TestQueryBiblePassage(t *testing.T) {
	doc := api.QueryBiblePassage("gen 1", "NIV")

	if doc == nil {
		t.Errorf("Could not retrieve bible passage")
	}
}

func TestQueryBibleLexicon(t *testing.T) {
	doc := api.QueryBibleLexicon("beginning", "NIV")

	if doc == nil {
		t.Errorf("Could not retrieve bible passage")
	}
}

// Database tests

// func TestOpenClient(t *testing.T) {
// 	var data bmul.SessionData

// 	ctx := context.Background()
// 	client := api.OpenClient(&ctx, data)

// 	if client == nil {
// 		t.Errorf("Could not open client")
// 	}
// }