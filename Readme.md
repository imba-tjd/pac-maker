# Pac Maker

* Generate `pac.txt` from `blocklist.txt` and `allowlist.txt`
* The pattern is simply suffix matching. `pac.js` is the logic. Minified by https://javascript-minifier.com
* List file contains one domain for a line, supporting comments(`#`)
* `null` seems to be faster than `undefined`; `JSON.parse` seems to be faster than directly define an object
* Inspired by the pac.txt from ssr
