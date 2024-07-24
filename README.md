# acr-qml-format
Extensão para validar formatação de código QML por meio da ferramenta qmlformat

Arquivo config.json

```json
{
    "stage": "static",
    "regexFile": ".*\\.qml",
    "regexIgnore": [
        ".*.qrc"
    ],
    "qmlFormat": {
        "command": "/bin/qmlformat",
        "arguments": ["--normalize", "--objects-spacing", "--functions-spacing"]
    }
}
```
