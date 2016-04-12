# colorbrewer_get_formatted

Given a permalink to a colorbrewer palette, download and format it for embedding in Matlab code.

example_usage:
```
$./python_utility_for_colorbrewer.py -p http://colorbrewer2.org/\?type\=sequential\&scheme\=YlGnBu\&n\=7  # print RGB formatted
[255 255 204;
 199 233 180;
 127 205 187;
 065 182 196;
 029 145 192;
 034 094 168;
 012 044 132];

$./python_utility_for_colorbrewer.py -pn http://colorbrewer2.org/\?type\=sequential\&scheme\=YlGnBu\&n\=7  # print rgb formatted
[1.000 1.000 0.800;
 0.780 0.914 0.706;
 0.498 0.804 0.733;
 0.255 0.714 0.769;
 0.114 0.569 0.753;
 0.133 0.369 0.659;
 0.047 0.173 0.518];

$./python_utility_for_colorbrewer.py -pnc http://colorbrewer2.org/\?type\=sequential\&scheme\=YlGnBu\&n\=7  # print rgb formatted and place result in clipboard
[1.000 1.000 0.800;
 0.780 0.914 0.706;
 0.498 0.804 0.733;
 0.255 0.714 0.769;
 0.114 0.569 0.753;
 0.133 0.369 0.659;
 0.047 0.173 0.518];
```

