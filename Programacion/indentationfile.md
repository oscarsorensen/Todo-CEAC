{
    "workbench.colorTheme": "Monokai Night",
    "editor.semanticHighlighting.enabled": false,
  
    "editor.tokenColorCustomizations": {
      "textMateRules": [
        {
          "scope": [
            "comment.line.number-sign.python",
            "comment.line.double-slash",
            "comment.block",
            "punctuation.definition.comment",
            "comment.block.documentation",
            "comment.line"
          ],
          "settings": {
            "foreground": "#49cf49",
            "fontStyle": ""
          }
        }
      ]
    },
  
    // === Built-in indentation and bracket visibility ===
    "editor.guides.indentation": true,
    "editor.guides.highlightActiveIndentation": true,
    "editor.bracketPairColorization.enabled": true,
    "editor.guides.bracketPairs": "active",
  
    // === Multi-color indentation guides (5 layers) ===
    "workbench.colorCustomizations": {
      // Each nesting level gets its own color
      "editorIndentGuide.background1": "#a61111",   // level 1 — red
      "editorIndentGuide.background2": "#c47f1c",   // level 2 — orange
      "editorIndentGuide.background3": "#c4c41c",   // level 3 — yellow
      "editorIndentGuide.background4": "#1cc41c",   // level 4 — green
      "editorIndentGuide.background5": "#1c7fc4",   // level 5 — blue
  
      // Active line highlight (brighter gray)
      "editorIndentGuide.activeBackground1": "#e85c5c",
      "editorIndentGuide.activeBackground2": "#ebb46a",
      "editorIndentGuide.activeBackground3": "#e8e86a",
      "editorIndentGuide.activeBackground4": "#6ae86a",
      "editorIndentGuide.activeBackground5": "#6aaee8",
  
      "editorRuler.foreground": "#666666"
    },
  
    // === Per-language overrides ===
    "[python]": { "editor.semanticHighlighting.enabled": false },
    "[html]": { "editor.semanticHighlighting.enabled": false },
    "[css]": { "editor.semanticHighlighting.enabled": false },
    "[javascript]": { "editor.semanticHighlighting.enabled": false },
    "[typescript]": { "editor.semanticHighlighting.enabled": false }
  }
  