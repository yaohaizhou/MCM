### 2021-2-6
1. latex macros
    - plain tex: `\def\macroname #1<sep>#2{expanded str, possibly containing #1,#2}`
        - 不检查该macro是否已经定义，直接覆盖
    - latex: `\newcommad`, `\renewcommand`
2. bib reference
    - count into toc: `\usepackage[nottoc]{tocbibind}`
    - add numbering like a chapter: `\usepackage[numbib]{tocbibind}`

### 2021-2-7
latex:
1. `\usepackage{indentfirst}`
2. counter, label:
    - `table`/`figure`/`section`... $\longleftrightarrow$ `\thetable`/`\thefigure`/`\thesection`
    - `\setcounter{table}{0}`
    - `\renewcommand{\thetable}{\alpha{table}}`
3. caption specifying:`caption`, `subcaption` package
    - overall: `font=small`
    - `labelfont=bf, textfont=normalfont`
    - `labelformat=simple, labelsep=period`

### 2021-2-8
latex:
1. toc depth:
    - globally, invariable: `\setcounter{tocdepth}{2}`
    - variable at place: `\usepackage{tocvsec2}`, `\settocdepth{subsection}`
2. toc spacing:
    - `\usepackage{setspace}`, `\begin{spacing}{0.1}`
3. `\autoref` in `hyperref` package
    - red brackets: `hidelinks`
    - rename: `\def\<type>autorefname{<newname>}`
4. align numbering: `\notag`/`\nonumber`, `\tag{blablabla}`

overleaf:
1. user mapping/marcro like vimrc: using tampermonkey script
```javascript
// ==UserScript==
// @name         Overleaf Editor Custom VIM Keybindings
// @namespace    http://tampermonkey.net/
// @version      0.1
// @match        https://www.overleaf.com/project/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    // poll until editor is loaded
    const retry = setInterval(() => {
        if (window._debug_editors === undefined) return
        clearInterval(retry)
        // get current editor instance
        const editor = window._debug_editors[window._debug_editors.length -1]
        // vim keyboard plugin
        const vimKeyboard = window.ace.require("ace/keyboard/vim")
        // add custom keybindings - insert mode applies on insert
        // normal mode applies while escaped
        vimKeyboard.Vim.map("j", "gj", "normal")
        vimKeyboard.Vim.map("k", "gk", "normal")
        // set the modified keyboard handler for editor
        editor.setKeyboardHandler(vimKeyboard.handler)
        console.log("Custom key bindings applied")
    }, 100)
})();
```


# 2021-2-9
1. newcommand: `\newcommand{\red}[1]{\textcolor{red}{#1}}`
    - `\renewcommand{\ref}[1]{Fig.\ref{#1}}` **failed** ?
2. appendix: `\usepackage[page,toc,titletoc,title]{appendix}`
    - page: Appendices start from a new page?
    - toc: Appendices start page added to toc
    - title: sections inside Appendices add `Appendix` before label
    - titletoc: similar to title, used in toc