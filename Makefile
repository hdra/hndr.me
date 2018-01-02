help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make build             generate site with relative paths            '
	@echo '   make serve             serve the output directory in a local server '
	@echo '   make publish.github    generate and publish the site to github pages'
	@echo '                                                                       '

build:
	pipenv run pelican content -o output -s pelicanconf.py -d

serve:
	cd output && pipenv run python -m pelican.server

publish.github:
	pipenv run pelican content -o output -s publishconf.py -v
	pipenv run ghp-import output
	git push origin gh-pages
