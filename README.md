# acr-qml-format
Extensão para validar formatação de código QML por meio da ferramenta qmlformat

Arquivo config.json

```json
{
    "regexFile": ".*\\.qml",
    "regexIgnore": [
        ".*.qrc"
    ],
    "message": "Indentação incorreta no arquivo ${FILE_PATH}",
    "qmlFormat": {
        "command": "/bin/qmlformat",
        "arguments": ["--normalize", "--objects-spacing", "--functions-spacing"]
    }
}
```
