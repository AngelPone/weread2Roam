// ==UserScript==
// @name         weread2clipboard
// @version      0.1
// @description  export weread highlights to clipboard
// @author       Ponez
// @match        https://weread.qq.com/*
// @grant        GM_registerMenuCommand
// @grant        GM_setClipboard
// ==/UserScript==

(function() {
    'use strict';
    const exportHighlights = () => {
        let highlight;
        let review;
        const bookName = document.getElementsByClassName('readerTopBar_title_link')[0].textContent
        const notesList = document.getElementsByClassName("readerNoteList")[0].getElementsByClassName('sectionListItem')
        var hightlights = ""
        for (let note of notesList) {
            var title = note.getElementsByClassName('sectionListItem_title')
            if (title.length == 1){
                if (title[0].textContent == '点评'){
                    continue
                }
                hightlights += `>>> #title ${title[0].textContent}\n`
            }
            var reviewDiv = note.getElementsByClassName('noteItem_content_review')
            if (reviewDiv.length == 1){
                highlight = reviewDiv[0].getElementsByClassName('abstract')[0].textContent
                review = reviewDiv[0].getElementsByClassName('text')[0].textContent
                hightlights += `>>> #highlight ${highlight} \n`
                hightlights += `>>> #fleeting ${review}\n`
                continue
            }
            var highlightDiv = note.getElementsByClassName('noteItem_content')
            if (highlightDiv.length == 1){
                highlight = highlightDiv[0].getElementsByClassName('text')[0].textContent
                hightlights += `>>> #highlight ${highlight}\n`
            }
        }
        GM_setClipboard(`>>> #bookName ${bookName}` + hightlights)
    }
    GM_registerMenuCommand('导出笔记', function() {
        exportHighlights()
    }, 'r');
})();