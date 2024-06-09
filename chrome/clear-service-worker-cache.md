# Clear Service Worker Cache

On macOS, you may discover the following folder with many GBs of data

`~/Library/Application Support/Google/Chrome/Default/Service Worker`.

In order to fix this, you need to
1. Stop Service workers
2. Uninstall Service Workers
3. Clear the cache

Keep in mind that you may need to do this for every profile that you use.

## How uninstall all service workers

1. Navigate to chrome://serviceworker-internals/
2. Open Developer Tools and go to the Console tab
3. Write `'allow paste'` in the console
4. Paste this snippet

```js
$$('.unregister').forEach(b => b.click())
````


## How to delete the Service Workers cache

If you just unregister the workers, the cache remains on the drive. If you just delete the cache, without first uninstalling the service worker, nothing will happen. You must first uninstall all service workers.

To delete the cache, after service workers are uninstalled

`Settings` -> `Privacy and security` -> `Clear browsing data` -> `All times` -> `Cookies and other site data`

