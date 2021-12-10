# acl2dash
ACL2 docset for Dash (http://kapeli.com/dash/)

## Steps to generate docset:
1. Download oringinal documents [here](https://www.cs.utexas.edu/users/moore/acl2/v8-4/combined-manual/download/index.html)
2. Use `xdata2html.pl` tool (in the downloaded document folder), to generate separate HTML files. Because the actual doc contents are in a gigantic JavaScript file (xdata.js).
3. Use `doc2set.py` (from this repo) to generate the database.

