package app

import (
	"errors"
	"fmt"
	"log"
	"strings"

	"github.com/julwrites/BotPlatform/pkg/platform"

	"github.com/julwrites/BotPlatform/pkg/def"
)

const (
	MCBRP string = "MCBRP"
	DJBRP string = "DJBRP"
	N5BRP string = "NTBRP"
	DGORG string = "DGORG"
)

const (
	BibleReadingPlan string = "BRP"
	DailyArticle     string = "DA"
)

var DEVO_NAMES = map[string]string{
	MCBRP: "M'Cheyne Bible Reading Plan",
	DJBRP: "Discipleship Journal Bible Reading Plan",
	N5BRP: "Navigators 5x5x5 New Testament Reading Plan",
	DGORG: "Desiring God Articles",
}

var DEVOS = map[string]string{
	"M'Cheyne Bible Reading Plan":                 MCBRP,
	"Discipleship Journal Bible Reading Plan":     DJBRP,
	"Navigators 5x5x5 New Testament Reading Plan": N5BRP,
	"Desiring God Articles":                       DGORG,
}

func AcronymizeDevo(msg string) (string, error) {
	msg = strings.Trim(msg, " ")
	devo, ok := DEVOS[msg]
	if ok {
		return devo, nil
	}
	return "", errors.New(fmt.Sprintf("Devo could not be recognized %s", msg))
}

func ExpandDevo(msg string) (string, error) {
	msg = strings.Trim(msg, " ")
	devo, ok := DEVO_NAMES[msg]
	if ok {
		return devo, nil
	}
	return "", errors.New(fmt.Sprintf("Devo could not be recognized %s", msg))
}

func GetDevotionalType(devo string) string {
	switch devo {
	case MCBRP:
		fallthrough
	case DJBRP:
		return BibleReadingPlan
	case N5BRP:
		return BibleReadingPlan
	case DGORG:
		return DailyArticle
	}

	return ""
}

func GetDevotionalText(devo string) string {
	var text string

	switch devo {
	case MCBRP:
		fallthrough // Same as DJBRP
	case DJBRP:
		text = "Here are today's Bible Reading passages, tap on any one to get the passage!"
	case N5BRP:
		text = "Here is today's Bible Reading passage!"
	case DGORG:
		break
	}

	return text
}

func GetDevotionalData(env def.SessionData, devo string) def.ResponseData {
	var response def.ResponseData

	response.Message = GetDevotionalText(devo)
	log.Printf("Got devotional text: %s", response.Message)

	switch devo {
	case MCBRP:
		response.Affordances.Options = GetMCheyneReferences()
		response.Affordances.Options = append(response.Affordances.Options, def.Option{Text: CMD_CLOSE})
	case DJBRP:
		response.Affordances.Options = GetDiscipleshipJournalReferences(env)
		if len(response.Affordances.Options) == 0 {
			response.Message = "Take this time today to reflect over this week's devotions"
		} else {
			response.Affordances.Options = append(response.Affordances.Options, def.Option{Text: CMD_CLOSE})
		}
	case N5BRP:
		response.Affordances.Options = GetNavigators5xReferences(env)
		if len(response.Affordances.Options) == 0 {
			response.Message = GetNavigators5xPrompt(env)
		} else {
			response.Affordances.Options = append(response.Affordances.Options, def.Option{Text: CMD_CLOSE})
		}
	case DGORG:
		response.Affordances.Options = GetDesiringGodArticles()
		response.Affordances.Inline = true
	default:
		response.Affordances.Remove = true
	}

	return response
}

func GetDevo(env def.SessionData) def.SessionData {
	switch env.User.Action {
	case CMD_DEVO:
		log.Printf("Detected existing action /devo")

		devo, err := AcronymizeDevo(env.Msg.Message)
		if err == nil {
			log.Printf("Devotional is valid, retrieving %s", devo)

			env.Res.Affordances.Remove = true
			env.Res.Message = "Just a moment..."

			platform.PostFromProps(env)

			// Retrieve devotional
			env.Res = GetDevotionalData(env, devo)

			env.User.Action = ""
		} else {
			log.Printf("AcronymizeDevo failed %v", err)
			env.Res.Message = "I didn't recognize that devo, please try again"
		}
	default:
		log.Printf("Activating action /devo")

		var options []def.Option

		for k, _ := range DEVOS {
			options = append(options, def.Option{Text: k})
		}
		options = append(options, def.Option{Text: CMD_CLOSE})

		env.Res.Affordances.Options = options

		env.User.Action = CMD_DEVO

		env.Res.Message = "Choose a Devotional to read!"
	}

	return env
}
