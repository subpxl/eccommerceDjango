from django.shortcuts import render
from .models import StoreFront

def home(request):
    context = {
        '':''
    }
    return render(request,'storefront/home.html',context)


def storefront(request,slug):
    storefront = StoreFront.objects.get(slug=slug)
    store = {

        "title":"Lannan Granite",
        "url":"http://localhost:8000/lallan-granite/",
        "short_description":"lallan mongo wale",
        "address":"171,sarkari aspatal k pass",
        "city":"los angeler",
        "pincode":"400040",
        "gmapLink":"https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12097.433213460943!2d-74.0062269!3d40.7101282!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xb89d1fe6bc499443!2sDowntown+Conference+Center!5e0!3m2!1smk!2sbg!4v1539943755621",
        "state":"california",
        "country":"usa",
        "phone":"0016666666",
        "email":"lallan@prasad.com",
        "youtubeLink":"https://www.youtube.com/watch?v=LXb3EKWsInQ",
        "menus":[
            {"name":"Home","link":"#home"},
            {"name":"Services","link":"#services"},
            {"name":"Portfolio","link":"#portfolio"},
            {"name":"About","link":"#about"},
            {"name":"Contact","link":"#contact"},
        ],
        "about":{
            "title":"this is about title",
            "brief":"about brief is here adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",

        },
        "featureTitle":"this is featureTitle",
        "featureSubTitle":"this is sub featureTitle",
        "features":
        [
            {"title":"this is title","subtitle":"this is subtitle"},
            {"title":"this is title","subtitle":"this is subtitle"},
            {"title":"this is title","subtitle":"this is subtitle"},
        ],
        "social":[
            {"name":"facebook","link":"facebook.com"},
            {"name":"instagram","link":"instagram.com"},
            {"name":"twitter","link":"twitter.com"},
            {"name":"linkedin","link":"linkedin.com"},
            {"name":"youtube","link":"youtube.com"},
        ],
        "services":[
            {"logo":"icon-box icon-box-pink","title":"Lorem Ipsum","subtitle":"Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate"},
            {"logo":"icon-box icon-box-yellow","title":"Sed ut perspiciatis","subtitle":"Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla"},
            {"logo":"icon-box icon-box-red","title":"Magni Dolores","subtitle":"Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim"},
            {"logo":"icon-box icon-box-blue","title":"Nemo Enim","subtitle":"At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum"},
        ],
        "testimonials":[
            {"review":"Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.","user":"Saul Goodman","title":"Ceo &amp; Founder","image":""},
            {"review":"Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.","user":"Saul Goodman","title":"Ceo &amp; Founder","image":""},
            {"review":"Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.","user":"Saul Goodman","title":"Ceo &amp; Founder","image":""},
            {"review":"Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.","user":"Saul Goodman","title":"Ceo &amp; Founder","image":""},

        ],
        "portfolio": [
            { "filter":"filter-app", "image":   "assets/img/portfolio/portfolio-1.jpg","link":"/link","title":"App 1"}, 
            { "filter":"filter-card", "image":   "assets/img/portfolio/portfolio-1.jpg","link":"/link","title":"App 1"}, 
            { "filter":"filter-web", "image":   "assets/img/portfolio/portfolio-1.jpg","link":"/link","title":"App 1"}, 
                ],      

            "callToAction":{
                "title":"Call To Action",
                "subtitle":"Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "button":"Click here",
                "link":"/",
            },
            "pricingPlan":[
                {}
            ]

    }
    
    context ={
        "storefront":storefront,
        "store":store
    }

    if storefront.type=="business":
        site = f'storefront/business/{storefront.theme}/index.html'
        return render(request,site,context)

    elif storefront.type=="shop":
        return render(request,'storefront/shop/shop.html',context)