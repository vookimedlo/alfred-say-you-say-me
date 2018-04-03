# alfred-say-you-say-me
[Alfred 3][1] workflow for saying a given text or a file content with a selected voice.

## Installation

1) Install [alfred-say-you-say-me workflow.][2]
2) All further updates are handled automatically.

## Usage

Select a UTF-8 encoded text file in finder and invoke the alfred file actions <kbd>⌃﻿⌘\\</kbd>.

![Alfred actions screenshot](doc/images/alfred-sayyousayme-screenshot_2018-04-03_20.53.12.png?raw=true "")

Choose the `Say...` in a displayed menu and select appropriate voice.

Then, the resulting file will appear in your `Desktop` directory. 

-------------------

Alternatively, you can pass the text you want to hear to this workflow. In Alfred, type `say` and pass the text as an argument.

![Alfred menu screenshot](doc/images/alfred-sayyousayme-screenshot_2018-04-03_20.49.18.png?raw=true "")

Then, select a voice and your text will be spoken. Voices are sorted by their locales and previously selected voices are prioritized. Notice, that each voice in a menu contains its locale, name and a localized voice introduction.

![Alfred voice menu screenshot](doc/images/alfred-sayyousayme-screenshot_2018-04-03_20.51.01.png?raw=true "")

-------------------

Have too many voices for a selection is pretty useless, so you can configure the language filter in a workflow configuration.
Fill all required locales in `language_filter` variable. Filter is case insensitive and is a regular expression. If you don't know what the regular expression is, just put there all locales divided by pipe symbol `|`. See the screenshot below.

![Alfred workflow configuration screenshot](doc/images/alfred-sayyousayme-screenshot_2018-04-03_20.51.32.png?raw=true "")

Then, you will see just voices which your languages support.

![Alfred filtered voice menu screenshot](doc/images/alfred-sayyousayme-screenshot_2018-04-03_20.52.14.png?raw=true "")

There is another variable you could set. It's a `buggy_voices_filter` variable, which contains a list of buggy voices. Currently, there is a [problem][3] in the Apple Synthetization Daemon and some voices can stick it. At the moment, only the `en_us - Alex` voice is added there. Again, list is a regular expression.

Stuck daemon could be unstuck by typing `.say-unstuck` in Alfred.

![Alfred actions screenshot](doc/images/alfred-sayyousayme-screenshot_2018-04-03_20.52.36.png?raw=true "")

[1]: https://www.alfredapp.com/
[2]: https://github.com/vookimedlo/alfred-say-you-say-me/releases/latest
[3]: https://www.applevis.com/forum/macos-mac-app-discussion/problem-using-spoken-track-service

