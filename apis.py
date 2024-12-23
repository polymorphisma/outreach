# The `api` dictionary is a configuration object that stores details for making HTTP requests to specific APIs.
# Each key in the dictionary corresponds to a unique API configuration.
# Each configuration contains:
# - `url`: The endpoint to which the request will be made.
# - `payload`: A dictionary of parameters that will be sent along with the request.
# - `headers`: A dictionary of HTTP headers to include in the request.
# - `method`: The HTTP method to use for the request (e.g., GET, POST).

# Example Usage:
# - To retrieve the configuration for the "test" API, you can access it like this:
#   method, url, payload, headers = return_values("test")
# - Then, you can use these details to make a request using the `request_method` function:
#   response = request_method(method=method, url=url, payload=payload, headers=headers)

cookie = "_cioid=6666e149b84d7103a16bd342;__qca=P0-1191032642-1730868150754;intercom-session-dyws6i9m=T0VYUDkxMGd5L01odzlqWmQ0MFd4aVNMTWNGRVlWNHBRM1BYWkUvK1pra3B5Q3NyWFcwbWJGMGFEZEVVQW5nSy0tRklVWUFNWHdSQ3pDblZ3T2kxVFVhQT09--c59b1fa06854ae9897f6a1025abbf5b6205983ed;mutiny.user.token=46664bb8-a67d-4fd5-8e9d-643f5e9dd6cd;_cioanonid=7847a9ab-525a-f920-7a59-f2d3e1847bf6;_fbp=fb.1.1723532442540.904732708794865942;__hssc=21978340.1.1734939870811;_hjSession_3601622=eyJpZCI6ImQ2MWYyZTZmLTEyZmMtNDFmZC1iOWY3LTMxNWIzYTNmY2YyYSIsImMiOjE3MzQ5Mzk4NDMzOTMsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=;_clsk=kkcjo5%7C1734939845878%7C1%7C1%7Cp.clarity.ms%2Fcollect;_tt_enable_cookie=1;__hstc=21978340.d66e4b739e51404853e7cae9a4af224d.1723532438952.1732594184916.1734939870811.17;_ga=GA1.1.1214073202.1723532441;_ga_76XXTC73SP=GS1.1.1734939843.12.0.1734939845.58.0.813187514;_uetvid=ae4e1200c10111ef803581b51efb9187;dwndvc=0f30091ac981b6e206d17e2d1a5ed845a4942e865b22c982152dd10673f154ca;GCLB=CKKrv7SFte-hFRAD;_gcl_au=1.1.1112617912.1732594162;ZP_LATEST_LOGIN_PRICING_VARIANT=23Q4_EC_Z59;ZP_Pricing_Split_Test_Variant=23Q4_EC_Z59;__cf_bm=Y1ZLV4QkQR_RWUTz7YWLs56Pj_1Fdt3kBV4yTt6DQNQ-1734939890-1.0.1.1-2m2Px61_lfm5GsqZtwVLruO_OWl9etMc5aT8khaXXi838nIdvA60.aWDL13FUV7AInyYYXVS9zogkPu2uzO1Pg;_dd_s=rum=0&expire=1734940874209;_uetsid=ae4de400c10111efa18b6b9febb5f143;zp__utm_source=(direct);dwnapijrn=94e45a9bb9b82f090e876f9d8b49489917f1b4ab312e17d5d0d93aff72782052;amplitude_id_122a93c7d9753d2fe678deffe8fac4cfapollo.io=eyJkZXZpY2VJZCI6IjhhNWNhODRhLTIzNTQtNDlhMy1iZDZmLTVmZWM0NDAwMGZiN1IiLCJ1c2VySWQiOiI2NjY2ZTE0OWI4NGQ3MTAzYTE2YmQzNDIiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE3MzQ5Mzk4NDI5NjUsImxhc3RFdmVudFRpbWUiOjE3MzQ5Mzk5NjQ2MzMsImV2ZW50SWQiOjI5MSwiaWRlbnRpZnlJZCI6MjM0LCJzZXF1ZW5jZU51bWJlciI6NTI1fQ==;__hssrc=1;__q_state_xnwV464CUjypYUw2=eyJ1dWlkIjoiOWM4NDVmOWEtMzgwNC00MWQwLWI4NWEtZjUyZTcwMDg1OTBhIiwiY29va2llRG9tYWluIjoiYXBvbGxvLmlvIiwiYWN0aXZlU2Vzc2lvbklkIjpudWxsLCJzY3JpcHRJZCI6IjEyMTc4MDAyNjk3MDcwNjA0NjYiLCJtZXNzZW5nZXJFeHBhbmRlZCI6ZmFsc2UsInByb21wdERpc21pc3NlZCI6ZmFsc2UsInN0YXRlQnlTY3JpcHRJZCI6eyIxMjE3ODAwMjY5NzA3MDYwNDY2Ijp7ImRpc21pc3NlZCI6ZmFsc2UsInNlc3Npb25JZCI6bnVsbH19LCJjb252ZXJzYXRpb25JZCI6IjE0NjAzNzUxMDIzMzk1NDAxODcifQ==;__stripe_mid=7bf642da-7545-4644-8cd1-07cba37e32add6f94c;_clck=1mupkm3%7C2%7Cfry%7C0%7C1686;_hjSessionUser_3601622=eyJpZCI6IjNiNGQ2NjZjLTM1NzUtNWI0MC04Y2JlLTkwMTg2NWRjNzYzNSIsImNyZWF0ZWQiOjE3MjM1MzI0NDM0NzEsImV4aXN0aW5nIjp0cnVlfQ==;_leadgenie_session=5nfRd9hKP3Yovrhzt%2F8EyZCx%2FPJGQjuV0M9wiQ5l%2Bgyu8%2B7%2F6En0ovC3FTrVdZBF7gFrqZz7kgAsjNVcetwle88j2bwfFmcCL%2Fl3Ck1IGMMtZJCs6W5gnlkfeWP%2F1i4SL3rP3HnSGaiYAUFWXn6K1Df514zwLGGRevdZie%2FqQasvhwzEkJV5LSLcLZmHeMkjKLdwsVCLRKAEbfqTHMFnzB1VN1ixYx6bmJdyFCLwGg6HFVN6MACGGsBBruSbleRK3Rjyna%2BhPx7lzKYbSrXn4S%2BHjniZNN0ZPKo%3D--CwIyZPgMa1fxNN3A--kk9yp6ALnWyspIVDAFCwGw%3D%3D;_ttp=5Et4TLemMODSba4WP1FLcbhw4SL.tt.1;blueID=0fb17c87-f75e-4772-8702-032817deff50;dwnapidvc=0906ada0e8fbdc4ffc42ee220a7f8c364c12d748efbdfb67dd744b9832b9311f;dwnjrn=ba9e968343eadb159e98ee2785216428de2b044ff0576800132c6d3d7c6b87ae;hubspotutk=d66e4b739e51404853e7cae9a4af224d;intercom-device-id-dyws6i9m=614b13c2-bb77-4077-b193-02aa8ca35e99;remember_token_leadgenie_v2=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqWTJOalpsTVRRNVlqZzBaRGN4TUROaE1UWmlaRE0wTWw5c1pXRmtaMlZ1YVdWamIyOXJhV1ZvWVhOb0lnPT0iLCJleHAiOiIyMDI0LTEyLTI2VDA0OjA5OjQ4LjU5NFoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdG9rZW5fbGVhZGdlbmllX3YyIn19--aff0c049dccb4dc81f004f9f556c02afd3d607ea;X-CSRF-TOKEN=RW_rfg4W3vI4c1k5URr1R116m9RSrwGwIAQ_RCuESOcv-scqnCwjR_PSsg9vAnw0I_qN1y3OxJYVjje9t1nurQ;zp__initial_landing_page=https://www.apollo.io/;zp__initial_utm_medium=(none);zp__initial_utm_source=(direct);zp__utm_medium=(none)"

titles = [
            "marketing",
            "seo",
            "content writer"
        ] # titles you want to scrape


HEADERS = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'cookie': cookie,
  'priority': 'u=1, i',
  'referer': 'https://app.apollo.io/',
  'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}

api_config = {
    "organization": {
        "url": "https://app.apollo.io/api/v1/organizations/search",
        "payload": {
            "display_mode": "fuzzy_select_mode",
            "cacheKey": "1730868633011"
        },
        "headers": HEADERS,
        "method": "GET",
        "required_values": ["q_organization_fuzzy_name"]
    },
    "people": {
        "url": "https://app.apollo.io/api/v1/mixed_people/search",
        "payload": {
            "finder_table_layout_id": "63bddc0106c6570001f131c1",
            "finder_view_id": "5b8050d050a3893c382e9360",
            "person_titles": titles,
            "page": 1,
            "sort_by_field": "recommendations_score",
            "display_mode": "explorer_mode",
            "per_page": 25,
            "open_factor_names": [],
            "num_fetch_result": 8,
            "context": "people-index-page",
            "show_suggestions": False,
            "finder_version": 1,
            "ui_finder_random_seed": "xwx9nfwgfx",
            "cacheKey": 1725274178893
        },
        "headers": {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'cookie': cookie,            
            'origin': 'https://app.apollo.io',
            'priority': 'u=1, i',
            'referer': 'https://app.apollo.io/',
            'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
            'x-csrf-token': '74l4CO2zzdl1k70V2nfvyBmssO-LnvwySzFhfs_JsmFzaAaWIoPJuNN8YhbCInwCPl8sfu9hg0i36aRFdRq3AQ'
        },
        "method": "POST",
        "required_values": ["organization_ids"]
    },
    "email": {
        "url": "https://app.apollo.io/api/v1/mixed_people/add_to_my_prospects",
        "payload": {
            # "entity_ids": [
            #     "6108c7f7c9ba5200010dfded"
            # ],
            "analytics_context": "Searcher: Individual Add Button",
            "skip_fetching_people": True,
            "cta_name": "Access email",
            "cacheKey": 1725275529911
        },
        "headers": {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'cookie': cookie,
            'origin': 'https://app.apollo.io',
            'priority': 'u=1, i',
            'referer': 'https://app.apollo.io/',
            'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
            'x-csrf-token': 'D1kDy3Pyr4DMD4C5RUeyH4y0Zx6_2-1g8yuvMPdoVLGTuH1VvMKr4WrgX7pdEiHVq0f7j9skkhoP82oLTbtR0Q'
        },
        "method": "POST",
        "required_values": ["entity_ids"]
    }
}
