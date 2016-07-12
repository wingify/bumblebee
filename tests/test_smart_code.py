# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @http://tasdikrahman.me

from unittest.mock import Mock
from unittest.mock import patch

from nose.tools import assert_equal

from bumblebee.vwo.smart_code import tracking_code


@patch('bumblebee.vwo.smart_code.requests.get')
def test_return_value_of_smart_code(mock_get):
    vwo_api_response = {'_data': {'async': '<!-- Start Visual Website Optimizer Asynchronous Code '
                    '-->\n'
                    "<script type='text/javascript'>\n"
                    'var _vwo_code=(function(){\n'
                    'var account_id=243020,\n'
                    'settings_tolerance=2000,\n'
                    'library_tolerance=2500,\n'
                    'use_existing_jquery=false,\n'
                    '// DO NOT EDIT BELOW THIS LINE\n'
                    'f=false,d=document;return{use_existing_jquery:function(){return '
                    'use_existing_jquery;},library_tolerance:function(){return '
                    'library_tolerance;},finish:function(){if(!f){f=true;var '
                    "a=d.getElementById('_vis_opt_path_hides');if(a)a.parentNode.removeChild(a);}},finished:function(){return "
                    'f;},load:function(a){var '
                    "b=d.createElement('script');b.src=a;b.type='text/javascript';b.innerText;b.onerror=function(){_vwo_code.finish();};d.getElementsByTagName('head')[0].appendChild(b);},init:function(){settings_timer=setTimeout('_vwo_code.finish()',settings_tolerance);var "
                    "a=d.createElement('style'),b='body{opacity:0 "
                    '!important;filter:alpha(opacity=0) '
                    '!important;background:none '
                    "!important;}',h=d.getElementsByTagName('head')[0];a.setAttribute('id','_vis_opt_path_hides');a.setAttribute('type','text/css');if(a.styleSheet)a.styleSheet.cssText=b;else "
                    "a.appendChild(d.createTextNode(b));h.appendChild(a);this.load('//dev.visualwebsiteoptimizer.com/j.php?a='+account_id+'&u='+encodeURIComponent(d.URL)+'&r='+Math.random());return "
                    'settings_timer;}};}());_vwo_settings_timer=_vwo_code.init();\n'
                    '</script>\n'
                    '<!-- End Visual Website Optimizer Asynchronous Code -->',
           'sync': '<!-- Start Visual Website Optimizer Synchronous Code -->\n'
                   "<script type='text/javascript'>\n"
                   'var _vis_opt_account_id = 243020;\n'
                   "var _vis_opt_protocol = (('https:' == "
                   "document.location.protocol) ? 'https://' : 'http://');\n"
                   'document.write(\'<s\' + \'cript src="\' + '
                   '_vis_opt_protocol +\n'
                   "'dev.visualwebsiteoptimizer.com/deploy/js_visitor_settings.php?v=1&a='+_vis_opt_account_id+'&url='\n"
                   '+encodeURIComponent(document.URL)+\'&random=\'+Math.random()+\'" '
                   'type="text/javascript">\' + \'<\\/s\' + \'cript>\');\n'
                   '</script>\n'
                   '\n'
                   "<script type='text/javascript'>\n"
                   'if(typeof(_vis_opt_settings_loaded) == "boolean") { '
                   'document.write(\'<s\' + \'cript src="\' + '
                   '_vis_opt_protocol +\n'
                   '\'d5phz18u4wuww.cloudfront.net/vis_opt.js" '
                   'type="text/javascript">\' + \'<\\/s\' + \'cript>\'); }\n'
                   '// if your site already has jQuery 1.4.2, replace '
                   'vis_opt.js with vis_opt_no_jquery.js above\n'
                   '</script>\n'
                   '\n'
                   "<script type='text/javascript'>\n"
                   'if(typeof(_vis_opt_settings_loaded) == "boolean" && '
                   'typeof(_vis_opt_top_initialize) == "function") {\n'
                   '        _vis_opt_top_initialize(); '
                   'vwo_$(document).ready(function() { '
                   '_vis_opt_bottom_initialize(); });\n'
                   '}\n'
                   '</script>\n'
                   '<!-- End Visual Website Optimizer Synchronous Code -->'}}

    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = vwo_api_response

    response = tracking_code()

    assert_equal(response.json(), vwo_api_response)
