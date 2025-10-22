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
    // Indentation colors
    "editorIndentGuide.background1": "#a61111",   // red
    "editorIndentGuide.background2": "#c47f1c",   // orange
    "editorIndentGuide.background3": "#c4c41c",   // yellow
    "editorIndentGuide.background4": "#1cc41c",   // green
    "editorIndentGuide.background5": "#1c7fc4",   // blue

    // Active indent highlights
    "editorIndentGuide.activeBackground1": "#e85c5c",
    "editorIndentGuide.activeBackground2": "#ebb46a",
    "editorIndentGuide.activeBackground3": "#e8e86a",
    "editorIndentGuide.activeBackground4": "#6ae86a",
    "editorIndentGuide.activeBackground5": "#6aaee8",

    "editorRuler.foreground": "#666666",

    // === Explorer panel ===
    "sideBar.background": "#1b1b1b",
    "sideBar.foreground": "#cccccc",
    "sideBarSectionHeader.background": "#202020",
    "sideBarSectionHeader.foreground": "#ffffff",

    // Tree line color (matches level 2 indent — orange)
    "tree.indentGuidesStroke": "#ce0f0f",

    // Slight tints to help visualize active/hovered folders
    "list.activeSelectionBackground": "#c47f1c20",
    "list.hoverBackground": "#c47f1c10",
    "list.inactiveSelectionBackground": "#c47f1c15",
    "list.highlightForeground": "#c47f1c",
    "list.activeSelectionForeground": "#ffffff",
    "list.hoverForeground": "#ffffff"
  },

  // === Per-language overrides ===
  "[python]": { "editor.semanticHighlighting.enabled": false },
  "[html]": { "editor.semanticHighlighting.enabled": false },
  "[css]": { "editor.semanticHighlighting.enabled": false },
  "[javascript]": { "editor.semanticHighlighting.enabled": false },
  "[typescript]": { "editor.semanticHighlighting.enabled": false }
}
