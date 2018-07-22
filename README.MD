
## Setup

```shell
brew update
xcode-select --install
sudo pip install --upgrade pip
sudo pip install scrapy --ignore-installed six
```

## Spiders

This project contains two spiders and you can list them using the `list`
command:

```shell
    $ scrapy list
```

## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

```shell
    $ scrapy crawl tag-webassembly
```
If you want to save the scraped data to a file, you can pass the `-o` option:

```shell    
    $ scrapy crawl tag-webassembly -o ./tmp/tag-webassembly.json
```