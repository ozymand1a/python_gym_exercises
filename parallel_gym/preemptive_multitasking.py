import time
import requests
import concurrent.futures


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('func:%r args:[%r, %r] took: %2.4f sec' % (method.__name__, args, kw, te - ts))
        return result

    return timed


def get_wiki_page_existence(wiki_page_url, timeout=10):
    response = requests.get(url=wiki_page_url, timeout=timeout)

    page_status = 'unknown'
    if response.status_code == 200:
        page_status = 'exist'
    elif response.status_code == 404:
        page_status = 'does not exist'

    return wiki_page_url + ' - ' + page_status


@timeit
def concurrent_wrapper(wiki_page_urls):
    # clean up threads quickly after execution
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        # send 4 tasks to executor block
        for url in wiki_page_urls:
            # return future exemplar
            futures.append(
                executor.submit(
                    get_wiki_page_existence, wiki_page_url=url
                )
            )
        for future in concurrent.futures.as_completed(futures):
            print(future.result())


@timeit
def concurrent_wrapper_with_exceptions(wiki_page_urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in wiki_page_urls:
            futures.append(
                executor.submit(
                    get_wiki_page_existence, wiki_page_url=url, timeout=0.00001
                )
            )
        for future in concurrent.futures.as_completed(futures):
            try:
                print(future.result())
            except requests.ConnectTimeout:
                print('ConnectTimeout.')


if __name__ == '__main__':

    # running without multithreading
    print('01. Base function to check wiki existence: ...')
    url = "https://en.wikipedia.org/wiki/Ocean"
    print(get_wiki_page_existence(wiki_page_url=url))

    # with multithreading
    wiki_page_urls = [
        "https://en.wikipedia.org/wiki/Ocean",
        "https://en.wikipedia.org/wiki/Island",
        "https://en.wikipedia.org/wiki/this_page_does_not_exist",
        "https://en.wikipedia.org/wiki/Shark",
    ]
    print('02. Base function with concurrent to check wiki existence: ...')
    concurrent_wrapper(wiki_page_urls)

    # with multithreading and exceptions
    print('03. Base function with concurrent and exceptions to check wiki existence: ...')
    concurrent_wrapper_with_exceptions(wiki_page_urls)

    # running without multithreading
    wiki_page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(10)]

    print("04. Running without threads:")
    without_threads_start = time.time()
    for url in wiki_page_urls:
        print(get_wiki_page_existence(wiki_page_url=url))
    print("Without threads time:", time.time() - without_threads_start)

    print("05. Running threaded:")
    threaded_start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in wiki_page_urls:
            futures.append(executor.submit(get_wiki_page_existence, wiki_page_url=url))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print("Threaded time:", time.time() - threaded_start)
