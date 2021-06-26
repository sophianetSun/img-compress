package main

import (
	"fmt"
	"time"

	"github.com/anthonynsimon/bild/imgio"
)

func main() {
	startTs := time.Now()
	img, err := imgio.Open("IMG_1576.PNG")
	if err != nil {
		fmt.Println(err)
		return
	}

	if err := imgio.Save("go_out.jpg", img, imgio.JPEGEncoder(85)); err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("elapsed: %s\n", time.Since(startTs))
}
