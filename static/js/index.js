// loads pageContent.json 
const pageContentJson = await fetch("./static/pageContent.json")
const pageContent = await pageContentJson.json()
const paragraphOne = pageContent["paragraphOne"]
const paragraphTwo = pageContent["paragraphTwo"]

// getting headers and paragraphs
const headers = document.getElementsByClassName("js-header")
const paragraphs = document.getElementsByClassName("js-paragraph")

// displaying paragraph content
headers[0].innerHTML = paragraphOne["headerOne"]
paragraphs[0].innerHTML = paragraphOne["paragraphContent"]
headers[1].innerHTML = paragraphTwo["headerTwo"]
paragraphs[1].innerHTML = paragraphTwo["paragraphContent"]
