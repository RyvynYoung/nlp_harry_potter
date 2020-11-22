# Imports

import pandas as pd
import numpy as np
from requests import get
from bs4 import BeautifulSoup
import os
import time
# scroll down for exercise functions

###### project functions #########
def make_soup(url):
    '''
    This helper function takes in a url and requests and parses HTML
    returning a soup object.
    '''
    # set headers and response variables
    headers = {'User-Agent': 'Codeup Data Science'} 
    response = get(url, headers=headers)
    # use BeartifulSoup to make object
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def github_HP_urls():
    '''
    This function scrapes all of the Harry Potter urls from
    the github search page and returns a list of urls.
    '''
    # get the first 100 pages to allow for those that don't have readme or language
    pages = range(1, 101)
    urls = []
    
    for p in pages:
        
        # format string of the base url for the main github search page we are using to update with page number
        url = f'https://github.com/search?p={p}&q=harry+potter&type=Repositories'

        # Make request and soup object using helper
        soup = make_soup(url)

        # Create a list of the anchor elements that hold the urls on this search page
        page_urls_list = soup.find_all('a', class_='v-align-middle')
        # for each url in the find all list get just the 'href' link
        page_urls = {link.get('href') for link in page_urls_list}
        # make a list of these urls
        page_urls = list(page_urls)
        # append the list from the page to the full list to return
        urls.append(page_urls)
        time.sleep(5)
        
    # flatten the urls list
    urls = [y for x in urls for y in x]
    return urls



def github_urls_single_page():
    '''
    This function scrapes all of the evironmental urls from
    the github first search page and returns a list of urls.
    '''
    # The base url for the main github search page we are using
    url = 'https://github.com/search?o=desc&p=1&q=environmental&s=&type=Repositories'
    
    # Make request and soup object using helper
    soup = make_soup(url)
    
    # Create a list of the anchor elements that hold the urls.
    urls_list = soup.find_all('a', class_='v-align-middle')
    # for each url in the find all list get just the 'href' link
    urls = {link.get('href') for link in urls_list}
    # make a list of these urls
    urls = list(urls)
    return urls
# this gets 1st 10 urls, will need to get next 10 pages



###### from Corey - NOT USED #######
def get_urls_list():
    '''
    This function collects Github repos when given a URL search page
    '''
    urls = ['https://github.com/freeCodeCamp/freeCodeCamp',
        'https://github.com/Famous/famous',
        'https://github.com/vuejs/vue',
        'https://github.com/kevana/ui-for-docker',
        'https://github.com/facebook/react',
        'https://github.com/ipython/ipython',
        'https://github.com/microsoft/TypeScript-Handbook',
        'https://github.com/airbnb/knowledge-repo',
        'https://github.com/rkern/line_profiler',
        'https://github.com/babel/babel-preset-env',
        'https://github.com/s3tools/s3cmd',
        'https://github.com/zzzeek/sqlalchemy',
        'https://github.com/thunil/TecoGAN',
        'https://github.com/l1ving/youtube-dl',
        'https://github.com/mdo/github-buttons',
        'https://github.com/StephenGrider/ReactNativeReduxCasts',
        'https://github.com/apollographql/apollo',
        'https://github.com/wandb/client',
        'https://github.com/RasaHQ/rasa_core',
        'https://github.com/angular-ui/angular-ui-OLDREPO',
        'https://github.com/urwid/urwid',
        'https://github.com/timqian/star-history',
        'https://github.com/PatrickJS/NG6-starter',
        'https://github.com/knrt10/kubernetes-basicLearning',
        'https://github.com/nature-of-code/noc-book',
        'https://github.com/erikbern/git-of-theseus',
        'https://github.com/dortania/OpenCore-Install-Guide',
        'https://github.com/Kapeli/Dash-User-Contributions',
        'https://github.com/github/docs',
        'https://github.com/StephenGrider/redux-code',
        'https://github.com/fossasia/meilix',
        'https://github.com/StephenGrider/EthereumCasts',
        'https://github.com/newren/git-filter-repo',
        'https://github.com/mateodelnorte/meta',
        'https://github.com/arsaboo/homeassistant-config',
        'https://github.com/IronLanguages/main',
        'https://github.com/StephenGrider/FullstackReactCode',
        'https://github.com/openworm/OpenWorm',
        'https://github.com/apache/nano',
        'https://github.com/jupyterhub/repo2docker',
        'https://github.com/abidrahmank/OpenCV2-Python-Tutorials',
        'https://github.com/Ceruleanacg/Personae',
        'https://github.com/mtdvio/ru-tech-chats',
        'https://github.com/xinntao/EDVR',
        'https://github.com/RubensZimbres/Repo-2017',
        'https://github.com/ipfs-inactive/js-ipfs-http-client',
        'https://github.com/browserpass/browserpass-legacy',
        'https://github.com/boston-dynamics/spot-sdk',
        'https://github.com/sourcerer-io/hall-of-fame',
        'https://github.com/blackorbird/APT_REPORT',
        'https://github.com/creationix/howtonode.org',
        'https://github.com/jennschiffer/make8bitart',
        'https://github.com/wdas/reposado',
        'https://github.com/guyzmo/git-repo',
        'https://github.com/Netflix/repokid',
        'https://github.com/nosarthur/gita',
        'https://github.com/harshjv/github-repo-size',
        'https://github.com/babel/babel-standalone',
        'https://github.com/kevin28520/My-TensorFlow-tutorials',
        'https://github.com/diyhue/diyHue',
        'https://github.com/StephenGrider/rn-casts',
        'https://github.com/headsetapp/headset-electron',
        'https://github.com/StijnMiroslav/top-starred-devs-and-repos-to-follow',
        'https://github.com/techgaun/active-forks',
        'https://github.com/donnemartin/viz',
        'https://github.com/tailwindlabs/tailwindui-vue',
        'https://github.com/GitGuardian/gg-shield',
        'https://github.com/dtschust/redux-bug-reporter',
        'https://github.com/burke-software/django-report-builder',
        'https://github.com/antsmartian/lets-build-express',
        'https://github.com/MicrosoftDocs/visualstudio-docs',
        'https://github.com/earwig/git-repo-updater',
        'https://github.com/OpenSourceTogether/Hacktoberfest-2020',
        'https://github.com/lightaime/deep_gcns_torch',
        'https://github.com/A3M4/YouTube-Report',
        'https://github.com/heroku/heroku-repo',
        'https://github.com/lambdaji/tf_repos',
        'https://github.com/StephenGrider/AdvancedReactNative',
        'https://github.com/lightaime/deep_gcns',
        'https://github.com/StephenGrider/DockerCasts',
        'https://github.com/mappum/gitbanner',
        'https://github.com/declare-lab/conv-emotion',
        'https://github.com/MarkWuNLP/MultiTurnResponseSelection',
        'https://github.com/chriswhong/nyctaxi',
        'https://github.com/18F/analytics-reporter',
        'https://github.com/npmhub/npmhub',
        'https://github.com/kesiev/akihabara',
        'https://github.com/ionic-team/ionic-site',
        'https://github.com/ros/rosdistro',
        'https://github.com/GoogleChromeLabs/tooling.report',
        'https://github.com/rpl/flow-coverage-report',
        'https://github.com/storybook-eol/react-native-storybook',
        'https://github.com/StephenGrider/MongoCasts',
        'https://github.com/kundajelab/deeplift',
        'https://github.com/microsoft/HealthClinic.biz',
        'https://github.com/Redocly/create-openapi-repo',
        'https://github.com/philbooth/complexity-report',
        'https://github.com/bensmithett/webpack-css-example',
        'https://github.com/PhantomInsights/mexican-government-report',
        'https://github.com/googlefonts/Inconsolata',
        'https://github.com/laincloud/lain',
        'https://github.com/auth0/repo-supervisor',
        'https://github.com/weightagnostic/weightagnostic.github.io',
        'https://github.com/jdorn/php-reports',
        'https://github.com/joeldenning/coexisting-vue-microfrontends']

    return urls



def get_github_HPresults(cached=False):
    '''
    This function with default cached == False does a fresh scrape of github pages returned from
    search of 'environmental' and writes the returned df to a json file.
    cached == True returns a df read in from a json file.
    '''
    # option to read in a json file instead of scrape for df
    if cached == True:
        df = pd.read_json('readmes.json')
        
    # cached == False completes a fresh scrape for df    
    else:
        # get url list
        url_list = github_HP_urls()

        # Set base_url that will be used in get request
        base_url = 'https://github.com'
        
        # List of full url needed to get readme info
        readme_url_list = []
        for url in url_list:
            full_url = base_url + url
            readme_url_list.append(full_url)
        
        # Create an empty list, readmes, to hold our dictionaries
        readmes = []

        for readme_url in readme_url_list:
            # Make request and soup object using helper
            soup = make_soup(readme_url)

            if soup.find('article', class_="markdown-body entry-content container-lg") != None:            
                # Save the text in each readme to variable text
                content = soup.find('article', class_="markdown-body entry-content container-lg").text
            
            if soup.find('span', class_="text-gray-dark text-bold mr-1") != None:
            # Save the first language in each readme to variable text
                # NOTE: this is the majority language, not all of the languages used
                language = soup.find('span', class_="text-gray-dark text-bold mr-1").text

                # anything else useful on the page?

                # Create a dictionary holding the title and content for each blog
                readme = {'language': language, 'content': content}

                # Add each dictionary to the articles list of dictionaries
                readmes.append(readme)
            
        # convert our list of dictionaries to a df
        df = pd.DataFrame(readmes)

        # Write df to a json file for faster access
        df.to_json('readmes.json')

    return df
    # 339 observations with 50 pgs
    # ... observations with 100 pgs

