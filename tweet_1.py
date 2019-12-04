import tweepy as tw
# from tweepy import Stream
# from tweepy.auth import OAuthHandler
# from tweepy.streaming import StreamListener
# from tweepy import API


ckey = 'zAiNJKEQE3Ekt5HO5lKLyczAF'
csecret = 'DMXUQVkRbrvOvEWrgqGOk7uDtYink55aw7fgelQ2PZHbJAmSVA'
atoken = '2871600776-LQbNzopvJFzBV1sNomGqi6eSyET80fQwoBXnsRq'
asecret = '06STLNoUWNlqlnOdPCMS17IgKGhtkHRRYd5hplefYGZ6A'
true = True
false = False

class listener(tw.StreamListener):

    def on_status(self, status):
        print("context == ", status.text)
        print("screen name == " + status.user.screen_name)
        return True

    def on_error(self, status):
        print(status)


auth = tw.OAuthHandler(ckey, csecret)

auth.set_access_token(atoken, asecret)


# twitterStream = tw.Stream(auth, listener())
# twitterStream.filter(follow=['1142414488395821056'])  # listening to a certain object
api = tw.API(auth, wait_on_rate_limit=True)
# api.update_status("大家好") # posting a tweet
# public_tweets = api.home_timeline()
Current = {
  "@http_status_code": 200,
  "@visible_sources": 23,
  "@available_sources": 169,
  "@persons_count": 1,
  "@search_id": "1912030249205587038353708928161883211",
  "query": {
    "emails": [
      {
        "@type": "personal",
        "address": "katelynnlynch91@gmail.com",
        "address_md5": "9db65d7a1c1895fc70831c8853f750e7"
      }
    ]
  },
  "available_data": {
    "premium": {
      "relationships": 17,
      "usernames": 3,
      "jobs": 5,
      "addresses": 11,
      "phones": 2,
      "mobile_phones": 1,
      "landline_phones": 1,
      "educations": 1,
      "languages": 1,
      "user_ids": 5,
      "social_profiles": 4,
      "names": 2,
      "dobs": 1,
      "images": 4,
      "genders": 1,
      "emails": 6
    }
  },
  "person": {
    "@id": "61874384-55f5-4f31-b5ba-5ff8d0a65252",
    "@match": 1,
    "@search_pointer": "7d3f80167fb1be7ee5da0ff5f63b729c6a5554cffefe48eafc41797e04d4baa5376c688c7abe3f0fa86ee288b6897f47c042662b00b839fd492b3544db49105c34c3f46389286ad04a1fe11b25209f45f578b18de6578c02d29938b52f6cfaf32482da845ac797a5ccf56b1adf004590b7fdb90ae8e488de36d3407c260b0f6e3dcdf612dfa5831ff83fb4c15405d083bc5e54b36b414ec94251e5aad63bffa8d88db9761859c793fbc76f85c50c68c843821a67a26c657de6f890a3a30948a6b8f2693282bf159623052f235876ce620eee8576c20546bd06f5548a6de360bec5da33b0b3f58d392cc96570eb9552937f64f825432ed4a7346cc6a2525ff1c0f73164a36c0db4ef60c11ff14a2a202432e0deff502897c056e753ec996fc07818c96c725c0dcc91d286239da96391838e607f1b0c7ce72a02884fedd5646daee88358e5614107eb6b875afa8f299448911bca46782cf06990e4b1884baf4244d3983a526896fdd1f17200ce6095de3a0ef2436d1b88196fa8d96a898f6ddf18a6b6b0cccd5630bf86ad52924c2825ea65813be82ccbfd5f34b4c43452dde9bb541e1b415a5666377042fce85b55560ba15c530f8769fb3e037c0525c061c309350bc0585a4df36768c2d19d07e009f48c9bd35815c1f28eb8ecf591c9f2219d10d9576343e9e4fd962bd451dc25d707157c252b8dc54cce4decb12f0bd5fc825a6e90c58054a87a1a39d4c06c67970e505c3fca082236fdb00ad5ab06fb0f3417163ab402a7769b8d8335b8c9faefcbc388e43721cf31d035928c2804ba0d3b4109c21715abb37c53b0248539d501b03d894483546f0a8d3c89f74da5509e877959ca3acab9427dde958adb3208511475d7e62b008dac48c1a0dffab2d6a2a1b6bd3bfc57d55ab20bd2bcd96a8c9e3bb9c85329517ee60cd221d4bf6c1d57a547a9810e73ef8b6349a06ab2f649807319c84b6b975a98c7102afba14604077ed24a0b1f321bf1c291af321d3aea914e0d6360b6900ba6a0f0fac7cac5b695f35ed7b249d0594351aa3ba2f233b3b2cf9b5a7388969d88df8114cafcca6b84faf1f6ac1855ef266ca140a9d72ee258956173cf1ed96365fc3b8739727998ee68efea8f15a593f80a5655aa51aa9e8767baab1834e053f3b8921d4a06fe5adf42d5e629105b36a026b8a75f5b686abbfdd489923ac1cd1d31ddb57c78d926976e7d3545c5ef6784c5e199d905beb8735fbc96c88bc99d879f064a3901df877c0081880fef7c2812fe9f583d901fc03a25f7ac767d72a35ec08a6cbc75aeb59146e0354f8b185c062e2e401907f25679c2b69850ae7d6f859405e298db8f2ed57836de692a87748a2ed78bd7089590bdb60aa2db9f02adec92b207ce37351535c599fb49a77974a82cf5fb765fb1c5662dd60c755a1876d914a3433bad493739021fd38e9f2cd75a36832625432664bd846c4a916f97d18ce75885c760bb41804f54adbec6f721a6ba8adaf2776d053ac4ad750666baa36b6edbeaec42c5811074d130b626b772c78af878d3ee923f4b462e6e96dbb3cc9f17632e31c4bb838972294c96922412982115186e53518743e44aaa774cb415f5ebcb02911bca23674f3302bf7614ae5036cdbb3db769111f82df460c0729073558b714324f31a0a516411c1d4073be649d50e8105144bcdc6b8338e0099fc34551bcf8fb3fa0256a63de441ad0d5add6c0021f3cd43d8c977a9fda7e87bc68725664ceccb46cb59b3b3f7181e1345b49a8c7af2fe7743df79ec0cc55526de5f00872a3511b478ba124405c8c0c7a74fd05e1c3180b7cb353dfa22a7d6f85282569db0ebd54a0ec0d224337b112c48989c704a97b51a6ca50983a682735000ecfd67f3fd919ea7da534529559d6d026e73fbe6cd44e7c60de5d1c6671b1b95fee6c48a7ab82e661b1ce81dea91a5b37f2bd6145e5d460a596c8927bfe1a2d35f6d16f773a077e111c743b4b380645ba594f532808248aaa31c6456275031eb22df618b447aaed824c6e9d39e8e29dc2099542d7365b41973ab22ca4748fc7cb3e35eb0e4ca477880f90a92f59dee68e2a685579a175b0afe4f2a76d5d7a1c45ba3407750da953d295da9e629058127bf031655076609f2455fe42241b7322ec1d982a923f36a037a669a3b3715dd2162d67f4974b84c975c4d61e3f8e28a60da4ed271c3c45b6d53954709c4cdd0726a74a2b9fe648e86bc7da750823cd3e7a69a1357365657d20d9a180cfd2ab8644439a4e5ba4a9965db348e4a09e152d02ff0449730a1f18d7ab3291f36801cafff0093ddee4042a4deda5adb2166baee177f8962830f122037caaa0deca73711c4b2882a3cd4efe2c6dc359789c538cbc160051cc2677d650734c97cff78a99116ab0cbf911e79f6283e5d314ca17e4af5eb6893e9b2820a9e4c71a4a04aa5a6f6572e4276159a268a255e9d6667a7e264b875a1df57aa07ee77a473ac1bdf077383f235c2ecf15b1e259303ec7cb78bfd194579bd9651fe7a1051e5dd248859b7c1006b67c5cd8c0066d2368d04dbf9ad7642fe0c036c0dfbdae725bb28ae8e4ec0a83ac79e515e0162502d84f13cd1657c62421277ab8550ee27a09b39e3104194d52c30627dca67a0c7e9527eb16557d9a0991f5872b260c6ba57da3911fee3eb7077ebc4d3001f72cbdd1fec16eae80d8eebb7b9f2c90581328e20ce7b71e79d0b5b676feb82a6f68f8fa54bf993c1a71e0bb8b8475fd61d323949171ff5e3de2758fda57a3b2cf2221f89236d3351607f8eee0a933f14469360d33234ce9e64e8ee5eec011d5a7dd84fb1cfdf4d4504e3cbb0cb7f943f8ccad4a761015382b207a1f0894be8cd2048e4a2538ab606c64fa034c463873081a8e4ceab653933d2ad7a62c4b5c61cccfade372ca582273c01e7aabc090b1e91538a9799101776a5b92594476bb29c02084fd6032f22f5c88d5ca1a50b6d8137177f3a0e75382fa24422bd67c5a92ccf86cb8ff50bc4a3fd64d74c9fdcbab0bb6b4a22790fc07376c5b259227bbd98e089bb9e2c9dab24ec9c3b0f419f75145f9f41f2e749a26f5edc35a486dfdcfd90d02762e79659576f9820817c001eef4ecfc74f586d49541454720167db42d119da31e1c0d2fad959b4b32ea1f366302e8e1291aa511fcb866ab39883f84d5a135c487ac25aacd3bfab7f84f38411b327f601fc3d202acb13710041d40848a48e557aa4ed369322a0d38e8d42e015dcf24737402ff7a0afc5096cb7e9abe2d3a561eec6bdee8e996ffdf585e615827207bceff1b6ff19a555d1e9edcc5a482629d46fb082c8a6f06145f448593f2a10d97db75bf9105dc157d61433093df336962548868c279db1b90272b1eca9d16c5c2f37edecefc0adcf0b0c5ee2baf2ea338745e1eefc66121f0633f1578e0073088af971e302671f8cde39eb8a3b841d3e5bb0fcd7a6985037df065e158e901c03e8ebe4cc20cb606cac17be0c6ffd9b40fc7616054d1786851fea71f5a2078174cf113a77c2c1e0e99ed019210d5c14e691ebaba977cc9c6a8d42d1f923914c783101cfb54c0ce10edc4f538b16cbd289d663fecdce09de64a91ba8eecd13f990b8a41534b21fcae9dfa43ee7821f5d268beb1e44351e49c7ab869bd74514963bfa69372db8b1d0f901304525ad6ddd4cd531983dc0fd81991d28e804da4b6874e51771fabd22364f9bacdb3bdbc1778cf90d4c0204c7a620d4cd5d555cb3e33ca184a4ef320e43df67b030572b56fc1799addbdd5ee1db8495540b582e3f2fdff93625b8239de87459fadec413ab5d14558fddbbf60107c3f0012903c58436888f22b6eb2b3e28c8c899aed66fe1adc37baadd2e6253570441983e9bde3b35e51a022e4b84f21669338b83d8ddf262e67abb027d917e4899490839e4a3d9fbfb7f5bbcd965ebe266789acbd939ac6ad0f0b6dcb617d88ccdfbc81db61f76f88f71126b96cbf003973c1dad7d0dc3697c4a1b78c8fbbe47e887d6868844ae82d7b09818bff1c6792dcc32d2aafb2025000ee7b5bf08b82acb293e2df372470389e458f84f08a523e85e7fd4db246e1fe3f7749811de6d5a8cc1f482f55aa35e4cd7a18ed7ae069bf383a2e087fd9365519e307dc1bfd97ca426a8a8683167e088e3fcd34580425c91fe905bee8069896f80abb81566806ed244c52fef95c6a4965b8b9da7e3c929ca5f8ff5920b3a53967936cf7e70611aa9524fd2afc772aaa45e97d139783fc47d5f436315c880893901d4cca79034b39bac60e87d2ed89879f34f2d5704cfa2911bc59f71345b577201615d0137ccce43bf21e8660652662f80462191c936552360fa78a2b5e1924b17f1e63d46c97b717c1c0ce83c1c88d920a082f07274fec3c596896afa8a2603dff01f0f95dc00c3a857eef439a7329629b6eecc8c4ff9dc8fb4ad3bcd5e1580283fff7dd30c2a42f600721d455fd4c91b9f4813f2cb3de3fa1852ab781ba1674b8b68ce9238906b96d99edce3c65721999eb72544ae85936d111e1d2e6fa32bcc5e2cbca5e8cf8004bf3cadea5830ce8025e2b823643d39774547ee8d434cdf9324e1ea6902b66b56ee1cdf131f934e974ba71d2d8c654fb23ce55e22cd92be63840f648039b2336513f7a2aa5dd447e360edaf2f697ea9056304d7d31a079d1c6f9593be06a0574370579f3c76e0a6f30d0c73a232d48cf4612b20079bcb6507afc8f54b46668dfa8412672538d7e7e341a42486b1363ad46aa6c8c2102e01e33fcecf4c7c7f3624e9b6b809943955194ba4cd0c45f927d11b354682101e218d3fec8a269c6ac646707c50c087f769f35080e204b3e3850db288f05e1addb744c38be5d303e039b819c131cc52a23f7b1329f2ca1b48cd48076c289e6ea6614ee354c4176cf6bb5a542fbed878dd363c7f6090de854afde14d7a98f00232e0667726ab584541636bf844086b19c896ac607fa6892c64913b8e4695c4b5b8706a935bdb408feb2135fc592509f1caf269b29c57af5fa92e74a50525f19deaa373932a314002066ad4288bc8f7307c4c8e9f8892bfb4355b3f9897848e42f3a2e56f20d316e0cf0276f495cc0ce1c47c00a2919c067ece5feb9e91402e95b1b553272f9114a2a7aa13d49a50cb993849a425358c267152cb76df45dd0d247dc22862452502d80b39eb69fdb58b2528817fa056fb155900d73ccb4547a064da2206690fd5f4ac295d57ae02751531dfe5d522a1f0e5bebec3f57d4ebb463a67cbd87159cbc6612f0bc6ae806ea61d4daae185396d89339fea9214a6e17ea2cf19f380ae845c030254885b7c8146785a06edaf9f632ff1f5a1db1a3c2fecebac1289f4dfe09904c85c66ada3de768cad399782c09107d19c4d046aa54df2fbe83a1949a741315749529ba1874e81b8eb5910d4289548ab433e7d35b71cf8fbf336c410f3c137e60e7155e6f2f06809ce06ee934a9d85482f074e7c9947df3092c0a6b637977f344fc6d5c460c89487e2762b958c7930d74b1753ef6b5dcbb8d44dc7e8298f83b6568ac471c8c61822410be230da87904ca64fa5f73d40c3fd6b1e54ccb3b5a69f38532ae37937672722302",
    "names": [
      {
        "@valid_since": "2008-01-01",
        "@last_seen": "2017-06-01",
        "prefix": "Ms",
        "first": "Katelynn",
        "middle": "Alexandra",
        "last": "Lynch",
        "display": "Katelynn Alexandra Lynch"
      },
      {
        "@valid_since": "2016-05-05",
        "@last_seen": "2018-11-14",
        "first": "Katelynn",
        "middle": "Lynch",
        "last": "Roberts",
        "display": "Katelynn Lynch Roberts"
      }
    ],
    "emails": [
      {
        "@valid_since": "2017-01-17",
        "@last_seen": "2017-01-17",
        "@type": "personal",
        "@email_provider": true,
        "address": "full.email.available@business.subscription",
        "address_md5": "9db65d7a1c1895fc70831c8853f750e7"
      },
      {
        "@valid_since": "2015-07-18",
        "@type": "personal",
        "@email_provider": true,
        "address": "full.email.available@business.subscription",
        "address_md5": "6eaaf194ba5b38a1b8221e9dbc9a4d47"
      },
      {
        "@valid_since": "2016-08-17",
        "@type": "personal",
        "@email_provider": true,
        "address": "full.email.available@business.subscription",
        "address_md5": "b2cc0c66469e569e00f9393049f0fe7d"
      },
      {
        "@valid_since": "2018-04-11",
        "@type": "personal",
        "@email_provider": true,
        "address": "full.email.available@business.subscription",
        "address_md5": "6d0c15c1b0d8aef11a92cb81492bda1b"
      },
      {
        "@valid_since": "2016-09-05",
        "@type": "personal",
        "@email_provider": true,
        "address": "full.email.available@business.subscription",
        "address_md5": "5e88bd9d1267e4bd86d25bc0e5f1a6c4"
      },
      {
        "@valid_since": "2018-09-06",
        "@type": "work",
        "@email_provider": false,
        "address": "full.email.available@business.subscription",
        "address_md5": "a6c6dac1bc6169437cfc7f43ca6746dc"
      }
    ],
    "usernames": [
      {
        "@valid_since": "2009-10-14",
        "content": "katelynn.lynch.9"
      },
      {
        "@valid_since": "2012-09-12",
        "content": "kalynch09"
      },
      {
        "@valid_since": "2013-04-09",
        "content": "katelynnlynch"
      }
    ],
    "phones": [
      {
        "@valid_since": "2006-07-16",
        "@type": "mobile",
        "country_code": 1,
        "number": 2817823049,
        "display": "281-782-3049",
        "display_international": "+1 281-782-3049"
      },
      {
        "country_code": 1,
        "number": 2403396756,
        "display": "240-339-6756",
        "display_international": "+1 240-339-6756"
      }
    ],
    "gender": {
      "@valid_since": "2010-11-17",
      "content": "female"
    },
    "dob": {
      "date_range": {
        "start": "1991-07-31",
        "end": "1991-07-31"
      },
      "display": "28 years old"
    },
    "languages": [
      {
        "@inferred": true,
        "region": "US",
        "language": "en",
        "display": "en_US"
      }
    ],
    "addresses": [
      {
        "@valid_since": "2008-01-01",
        "@type": "work",
        "country": "US",
        "state": "KY",
        "city": "Lexington",
        "street": "Henderson Drive",
        "house": "840",
        "zip_code": "40515",
        "display": "840 Henderson Drive, Lexington, Kentucky"
      },
      {
        "@valid_since": "2015-07-18",
        "country": "US",
        "state": "KY",
        "city": "Madisonville",
        "street": "N Seminary Street",
        "house": "326",
        "zip_code": "42431",
        "display": "326 N Seminary Street, Madisonville, Kentucky"
      },
      {
        "@valid_since": "2018-04-11",
        "country": "US",
        "state": "KY",
        "city": "Madisonville",
        "street": "Lawrence Street",
        "house": "352",
        "zip_code": "42431",
        "display": "352 Lawrence Street, Madisonville, Kentucky"
      },
      {
        "@valid_since": "2017-11-07",
        "country": "US",
        "state": "KY",
        "city": "Madisonville",
        "street": "Wiman Drive",
        "house": "314",
        "zip_code": "42431",
        "display": "314 Wiman Drive, Madisonville, Kentucky"
      },
      {
        "@valid_since": "2016-08-17",
        "country": "US",
        "state": "KY",
        "city": "Madisonville",
        "street": "Hanson Street",
        "house": "609",
        "zip_code": "42431",
        "display": "609 Hanson Street, Madisonville, Kentucky"
      },
      {
        "@valid_since": "2006-07-16",
        "@last_seen": "2018-11-14",
        "@type": "work",
        "country": "US",
        "state": "TX",
        "city": "Angleton",
        "street": "Meadowlark Lane",
        "house": "100",
        "zip_code": "77515",
        "display": "100 Meadowlark Lane, Angleton, Texas"
      },
      {
        "@valid_since": "2006-07-16",
        "@last_seen": "2018-11-14",
        "@type": "work",
        "country": "US",
        "state": "TX",
        "city": "Freeport",
        "display": "Freeport, Texas"
      },
      {
        "@valid_since": "2006-07-16",
        "@last_seen": "2018-11-14",
        "country": "US",
        "state": "TX",
        "city": "Houston",
        "display": "Houston, Texas"
      },
      {
        "@valid_since": "2006-07-16",
        "country": "US",
        "state": "TX",
        "city": "Danbury",
        "display": "Danbury, Texas"
      },
      {
        "@valid_since": "2018-09-06",
        "country": "US",
        "state": "TX",
        "city": "Angleton",
        "street": "Technology Road",
        "house": "4005",
        "zip_code": "77515",
        "display": "4005 Technology Road, Angleton, Texas"
      },
      {
        "country": "US",
        "state": "MD",
        "display": "Maryland, United States"
      }
    ],
    "jobs": [
      {
        "@valid_since": "2016-05-05",
        "@last_seen": "2018-11-14",
        "title": "Environmental Scientist",
        "organization": "AECOM",
        "date_range": {
          "start": "2016-04-01"
        },
        "display": "Environmental Scientist at AECOM (since 2016)"
      },
      {
        "@valid_since": "2016-05-05",
        "@last_seen": "2018-11-14",
        "title": "Environmental Data and Information Management- System Admin Tech",
        "organization": "Kelly Services at The Dow Chemical Company",
        "date_range": {
          "start": "2014-09-01",
          "end": "2016-04-01"
        },
        "display": "Environmental Data and Information Management- System Admin Tech at Kelly Services at The Dow Chemical Company (2014-2016)"
      },
      {
        "@valid_since": "2014-01-01",
        "title": "Dow Chemical Environmental Data and Information Management- Materials Team System Admin Tech",
        "organization": "Kelly Services",
        "date_range": {
          "start": "2014-09-01"
        },
        "display": "Dow Chemical Environmental Data and Information Management- Materials Team System Admin Tech at Kelly Services (since 2014)"
      },
      {
        "@valid_since": "2014-01-01",
        "@last_seen": "2018-11-14",
        "title": "Administrative Assistant",
        "organization": "JIT Distributing",
        "date_range": {
          "start": "2013-08-01",
          "end": "2014-08-01"
        },
        "display": "Administrative Assistant at JIT Distributing (2013-2014)"
      },
      {
        "@valid_since": "2006-07-16",
        "organization": "LYNCHS GARAGE",
        "display": "LYNCHS GARAGE"
      }
    ],
    "educations": [
      {
        "@valid_since": "2014-01-01",
        "@last_seen": "2018-11-14",
        "degree": "Bachelor of Science (BS), Environmental Management",
        "school": "University of Houston-Clear Lake",
        "date_range": {
          "start": "2012-01-01",
          "end": "2014-12-31"
        },
        "display": "Bachelor of Science (BS), Environmental Management from University of Houston-Clear Lake (2012-2014)"
      }
    ],
    "relationships": [
      {
        "@type": "family",
        "names": [
          {
            "first": "James",
            "middle": "Edward",
            "last": "Lynch",
            "display": "James Edward Lynch"
          }
        ]
      },
      {
        "@type": "family",
        "names": [
          {
            "first": "Laura",
            "middle": "Alayne",
            "last": "Lynch",
            "display": "Laura Alayne Lynch"
          }
        ]
      },
      {
        "@type": "family",
        "names": [
          {
            "first": "Steven",
            "middle": "Patrick",
            "last": "Lynch",
            "display": "Steven Patrick Lynch"
          }
        ]
      },
      {
        "@type": "family",
        "names": [
          {
            "first": "Ida",
            "middle": "F",
            "last": "Lynch",
            "display": "Ida F Lynch"
          }
        ]
      },
      {
        "@type": "family",
        "names": [
          {
            "first": "Rebecca",
            "middle": "Lynn",
            "last": "Peltier",
            "display": "Rebecca Lynn Peltier"
          }
        ]
      },
      {
        "@type": "family",
        "names": [
          {
            "first": "Aaron",
            "middle": "Cole",
            "last": "Roberts",
            "display": "Aaron Cole Roberts"
          }
        ]
      },
      {
        "@valid_since": "2009-10-14",
        "@type": "other",
        "names": [
          {
            "@valid_since": "2009-10-14",
            "first": "Vijay",
            "middle": "Jacob",
            "last": "Abraham",
            "display": "Vijay Jacob Abraham"
          }
        ]
      },
      {
        "@valid_since": "2010-06-03",
        "@type": "other",
        "names": [
          {
            "@valid_since": "2010-06-03",
            "first": "Rowin",
            "last": "Meth",
            "display": "Rowin Meth"
          }
        ]
      },
      {
        "@valid_since": "2010-06-01",
        "@type": "other",
        "names": [
          {
            "@valid_since": "2010-06-01",
            "first": "Frannie",
            "last": "Vollbaum",
            "display": "Frannie Vollbaum"
          }
        ]
      },
      {
        "@valid_since": "2010-06-01",
        "@type": "other",
        "names": [
          {
            "@valid_since": "2010-06-01",
            "first": "Mark",
            "last": "Rodriguez",
            "display": "Mark Rodriguez"
          }
        ]
      },
      {
        "@valid_since": "2010-06-01",
        "@type": "other",
        "names": [
          {
            "@valid_since": "2010-06-01",
            "first": "Chris",
            "last": "Ryan",
            "display": "Chris Ryan"
          }
        ]
      },
      {
        "@valid_since": "2010-06-01",
        "@type": "other",
        "names": [
          {
            "@valid_since": "2010-06-01",
            "first": "Juan",
            "last": "Delgado",
            "display": "Juan Delgado"
          }
        ]
      },
      {
        "@valid_since": "2010-06-01",
        "@type": "other",
        "names": [
          {
            "@valid_since": "2010-06-01",
            "first": "Cody",
            "last": "Winters",
            "display": "Cody Winters"
          }
        ]
      },
      {
        "@valid_since": "2010-06-01",
        "@type": "other",
        "names": [
          {
            "@valid_since": "2010-06-01",
            "first": "Sean",
            "last": "Bruemmer",
            "display": "Sean Bruemmer"
          }
        ]
      },
      {
        "@valid_since": "2010-06-01",
        "@type": "other",
        "names": [
          {
            "@valid_since": "2010-06-01",
            "first": "Meagan",
            "last": "Harvey",
            "display": "Meagan Harvey"
          }
        ]
      },
      {
        "@valid_since": "2009-10-24",
        "@type": "other",
        "names": [
          {
            "@valid_since": "2009-10-24",
            "first": "Chase",
            "last": "Sanders",
            "display": "Chase Sanders"
          }
        ]
      },
      {
        "@valid_since": "2010-06-01",
        "@type": "other",
        "names": [
          {
            "@valid_since": "2010-06-01",
            "first": "Jared",
            "last": "Brimage",
            "display": "Jared Brimage"
          }
        ]
      }
    ],
    "user_ids": [
      {
        "@valid_since": "2014-01-01",
        "@last_seen": "2018-11-14",
        "content": "6a/2b1/5b5@linkedin"
      },
      {
        "@valid_since": "2009-10-14",
        "content": "512512526@facebook"
      },
      {
        "@valid_since": "2013-04-09",
        "content": "423941786@twitter"
      },
      {
        "@valid_since": "2014-01-01",
        "@last_seen": "2018-11-14",
        "content": "245579033@linkedin"
      },
      {
        "@valid_since": "2014-01-01",
        "@last_seen": "2018-11-14",
        "content": "#5b52b16a@linkedin"
      }
    ],
    "images": [
      {
        "@valid_since": "2009-10-14",
        "url": "http://graph.facebook.com/512512526/picture?type=large",
        "thumbnail_token": "AE2861B242686E6ACBCD539D133B8AE59A9AE962DB1FA5AA7AF089AADD6808FB1E61839A86D4B8252BD8922E00649241641F52F0B958D11ED09075115311196AF5"
      },
      {
        "@valid_since": "2016-01-13",
        "url": "https://s-media-cache-ak0.pinimg.com/avatars/kalynch09_1337064340_140.jpg",
        "thumbnail_token": "AE2861B20B7D6E22CA814E9059348AAB9C99E565D51CA7AE27F1CCF2813454AE0530DAD8D9DCAD302ACB85625B768348201D50EAEE04A84B90CA261C561C126DF5F6C13401FF2AFA0052B2A8CEE3ADE6EBC5EB78"
      },
      {
        "@valid_since": "2018-06-26",
        "@last_seen": "2018-06-26",
        "url": "https://media.licdn.com/dms/image/C5603AQGUyQKYmU_STA/profile-displayphoto-shrink_200_200/0?e=1535587200&v=beta&t=Xvt4Fb58Ea489J3B5_6tqwTAuE5TRC8vwK_IgLH49CM",
        "thumbnail_token": "AE2861B20B7D6E22D4C9479C5C7387EF9C9CE823D35EABEA73B2CFB4863058AE4E7CF680C08DE8100FEDA2682556BB490C2C60D69F128708CC9F784005054530B6D99C6148A128E5131BFBA8CFF5F9BDB5A8E97CF99A12DD7A9948B1D92730DCE7C5B74B5A526211CCC892B90151753EF5025EFFDCE6E10B6E70C3A646C9A98F1503E9156104AE6A2E36AA642E15A40F78599135285CE84C02FBDF2FF43EB38D8D8373FBD7"
      },
      {
        "@valid_since": "2013-04-09",
        "url": "http://pbs.twimg.com/profile_images/2795624305/fd4102500cf595c8ece165549b686828.jpeg",
        "thumbnail_token": "AE2861B242686E7DDBDF0D814A3486E1D19BE9609F41B4AA71B6D0FEB03454A84C36C69AC48AE2646898C3224428CD423D4702B2EC08C74AC09F2415554B193CA6CCC13604E474B30542EEED9FB5A8FDB487BE2BEFA153842E8B4BB7842E35"
      }
    ],
    "urls": [
      {
        "@source_id": "318049613a49419f54520686b904a708",
        "@domain": "linkedin.com",
        "@name": "LinkedIn",
        "@category": "professional_and_business",
        "url": "https://www.linkedin.com/in/katelynn-roberts-5b52b16a"
      },
      {
        "@source_id": "54e8896cac9bfa43401395745b15d3ae",
        "@domain": "facebook.com",
        "@name": "Facebook",
        "@category": "personal_profiles",
        "url": "http://www.facebook.com/people/_/512512526"
      },
      {
        "@source_id": "d8f5ff24c201a4c6aeaec9a7e17454b0",
        "@domain": "pinterest.com",
        "@name": "Pinterest",
        "@category": "personal_profiles",
        "url": "http://pinterest.com/kalynch09/"
      },
      {
        "@source_id": "73710d6d832c2e7d73daaeb24be5a2a0",
        "@domain": "twitter.com",
        "@name": "Twitter",
        "@category": "personal_profiles",
        "url": "http://www.twitter.com/KatelynnLynch"
      },
      {
        "@source_id": "32e09ebd1bc0121b2c4e2295d7151a31",
        "@sponsored": true,
        "@domain": "tracking.instantcheckmate.com",
        "@name": "Instant Checkmate",
        "@category": "background_reports",
        "url": "http://tracking.instantcheckmate.com/?a=60&c=148&city=Danbury&cmp=SB_MultiR&fname=Katelynn&lname=Lynch&mdm=api&oc=5&s1=Mshortcut_results&s1=SB_MultiR&s2=3&s4=results&s5=09292017-00&src=pipl&state=TX"
      },
      {
        "@source_id": "554ee756ab454f84cc0e77a182311264",
        "@sponsored": true,
        "@domain": "tracking.instantcheckmate.com",
        "@name": "Instant Checkmate",
        "@category": "background_reports",
        "url": "http://tracking.instantcheckmate.com/?a=60&c=148&city=Danbury&cmp=SB_MultiR&fname=Katelynn&lname=Roberts&mdm=api&oc=5&s1=Mshortcut_results&s1=SB_MultiR&s2=3&s4=results&s5=09292017-01&src=pipl&state=TX"
      },
      {
        "@valid_since": "2014-01-01",
        "@domain": "facebook.com",
        "@category": "personal_profiles",
        "url": "http://www.facebook.com/katelynn.lynch.9"
      }
    ]
  }
}
# user = api.get_user('HuangSicong')
# friends = user.friends() # getting user's friends
# for person in friends:
#     print(person.screen_name, person.name)
# print(api.user_timeline('Dave2D'))  # getting user timeline
# for item in Current['person']['urls']:
#     if url in item and (item['url'] is 'Twitter'):
#         print(item['url'])
print('hi')
asd = api.user_timeline('Dave2D')
if 'usernames' in Current['person']:
    for item in Current['person']['usernames']:
        try:
            asd = api.user_timeline(item['content'])
            for each in asd:
                print(each.text)
        except:
            print(item['content'])
            # print(api.user_timeline(item['content']))

print(Current['person']['urls'][3]['url'])
# for e in api.user_timeline('Dave2D'):
#     print("tweet == ", e.text)
# print(api.friends('Dave2D'))    # getting friends
# for e in api.friends('Dave2D'):
#     print(e.screen_name, e.name)
