# Run unsigned apps

Apple requires that all `*.app` packages have to be signed by a "known" developer. It basically requires that the author of the app has an Apple Developer Account ($100/year) and signs the app prior to distribution. That is a **good** thing, as it prevents the spread of malware. However, sometime you may want to run your own apps. For those cases, you can run this command first to allow the app to be opened perpetually thereafter

```bash
xattr -dr com.apple.quarantine "/Applications/<YourApp>.app"
```
