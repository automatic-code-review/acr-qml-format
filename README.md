# acr-qml-format

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
