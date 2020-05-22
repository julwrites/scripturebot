// Brief: Main entry point of the bot Web App
// Primary responsibility: Receive and identify handler to delegate to

package scripturebot

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"path/filepath"
	"strings"

	botsecrets "github.com/julwrites/BotSecrets"
)

func bothandler(res http.ResponseWriter, req *http.Request) {
	secretsPath, _ := filepath.Abs("./secrets.yaml")
	secrets := botsecrets.LoadSecrets(secretsPath)

	switch strings.Trim(req.URL.EscapedPath(), "\n") {
	case strings.Trim("/"+secrets.TELEGRAM_ID, "\n"):
		log.Printf("Incoming telegram message")
		TelegramHandler(res, req, &secrets)
	default:
		log.Fatalf("No appropriate handler")
	}
}

func main() {
	http.HandleFunc("/", bothandler)

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
		log.Printf("Defaulting to port %s", port)
	}

	log.Printf("Listening on port %s", port)
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%s", port), nil))
}
