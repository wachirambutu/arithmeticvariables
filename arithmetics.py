
<!DOCTYPE html>
<html  dir="ltr" lang="en" xml:lang="en">
<head>
    <title>Zetech Digital School</title>
   	<link rel="shortcut icon" href="//elearning.zetech.ac.ke/pluginfile.php/1/theme_mb2iq/favicon/1610721501/favicon.ico" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="//fonts.googleapis.com/css?family=Nunito+Sans:300,400,700" rel="stylesheet">    	    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="moodle, Zetech Shit School" />
<link rel="stylesheet" type="text/css" href="https://elearning.zetech.ac.ke/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" /><script id="firstthemesheet" type="text/css">/** Required in order to fix style inclusion problems in IE with YUI **/</script><link rel="stylesheet" type="text/css" href="https://elearning.zetech.ac.ke/theme/styles.php/mb2iq/1610721501_1/all" />
<link rel="stylesheet" type="text/css" href="https://elearning.zetech.ac.ke/theme/mb2iq/assets/pe-icon-7-stroke/css/pe-icon-7-stroke.min.css" />
<link rel="stylesheet" type="text/css" href="https://elearning.zetech.ac.ke/theme/mb2iq/assets/bootstrap/css/glyphicons.min.css" />
<link rel="stylesheet" type="text/css" href="https://elearning.zetech.ac.ke/theme/mb2iq/assets/OwlCarousel/assets/owl.carousel.min.css" />
<script>
//<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/elearning.zetech.ac.ke","sesskey":"C3sTAu9YPX","sessiontimeout":"28800","themerev":"1610721501","slasharguments":1,"theme":"mb2iq","iconsystemmodule":"core\/icon_system_fontawesome","jsrev":"1610711879","admin":"admin","svgicons":true,"usertimezone":"Africa\/Nairobi","contextid":2,"langrev":1610711879,"templaterev":"1610711879"};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''}
if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else{me.path=component+'/'+component+'.'+me.type}};
YUI_config = {"debug":false,"base":"https:\/\/elearning.zetech.ac.ke\/lib\/yuilib\/3.17.2\/","comboBase":"https:\/\/elearning.zetech.ac.ke\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/elearning.zetech.ac.ke\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/elearning.zetech.ac.ke\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/elearning.zetech.ac.ke\/theme\/yui_combo.php?m\/1610711879\/","combine":true,"comboBase":"https:\/\/elearning.zetech.ac.ke\/theme\/yui_combo.php?","ext":false,"root":"m\/1610711879\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-popuphelp":{"requires":["moodle-core-tooltip"]},"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-tooltip":{"requires":["base","node","io-base","moodle-core-notification-dialogue","json-parse","widget-position","widget-position-align","event-outside","cache-base"]},"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-formchangechecker":{"requires":["base","event-focus","moodle-core-event"]},"moodle-core-languninstallconfirm":{"requires":["base","node","moodle-core-notification-confirm","moodle-core-notification-alert"]},"moodle-core_availability-form":{"requires":["base","node","event","event-delegate","panel","moodle-core-notification-dialogue","json"]},"moodle-backup-confirmcancel":{"requires":["node","node-event-simulate","moodle-core-notification-confirm"]},"moodle-backup-backupselectall":{"requires":["node","event","node-event-simulate","anim"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-course-formatchooser":{"requires":["base","node","node-event-simulate"]},"moodle-form-passwordunmask":{"requires":[]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-question-preview":{"requires":["base","dom","event-delegate","event-key","core_question_engine"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_attendance-groupfilter":{"requires":["base","node"]},"moodle-mod_bigbluebuttonbn-rooms":{"requires":["base","node","datasource-get","datasource-jsonschema","datasource-polling","moodle-core-notification"]},"moodle-mod_bigbluebuttonbn-modform":{"requires":["base","node"]},"moodle-mod_bigbluebuttonbn-recordings":{"requires":["base","node","datasource-get","datasource-jsonschema","datasource-polling","moodle-core-notification"]},"moodle-mod_bigbluebuttonbn-broker":{"requires":["base","node","datasource-get","datasource-jsonschema","datasource-polling","moodle-core-notification"]},"moodle-mod_bigbluebuttonbn-imports":{"requires":["base","node"]},"moodle-mod_customcert-rearrange":{"requires":["dd-delegate","dd-drag"]},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-util":{"requires":["node","moodle-core-actionmenu"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-filter_glossary-autolinker":{"requires":["base","node","io-base","json-parse","event-delegate","overlay","moodle-core-event","moodle-core-notification-alert","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-filter_mathjaxloader-loader":{"requires":["moodle-core-event"]},"moodle-editor_atto-editor":{"requires":["node","transition","io","overlay","escape","event","event-simulate","event-custom","node-event-html5","node-event-simulate","yui-throttle","moodle-core-notification-dialogue","moodle-core-notification-confirm","moodle-editor_atto-rangy","handlebars","timers","querystring-stringify"]},"moodle-editor_atto-plugin":{"requires":["node","base","escape","event","event-outside","handlebars","event-custom","timers","moodle-editor_atto-menu"]},"moodle-editor_atto-menu":{"requires":["moodle-core-notification-dialogue","node","event","event-custom"]},"moodle-editor_atto-rangy":{"requires":[]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-gradereport_grader-gradereporttable":{"requires":["base","node","event","handlebars","overlay","event-hover"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-tool_capability-search":{"requires":["base","node"]},"moodle-tool_lp-dragdrop-reorder":{"requires":["moodle-core-dragdrop"]},"moodle-tool_monitor-dropdown":{"requires":["base","event","node"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","transition","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-alert","moodle-core-notification-warning","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-atto_accessibilitychecker-button":{"requires":["color-base","moodle-editor_atto-plugin"]},"moodle-atto_accessibilityhelper-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_align-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_bold-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_charmap-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_clear-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_collapse-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emojipicker-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emoticon-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_equation-button":{"requires":["moodle-editor_atto-plugin","moodle-core-event","io","event-valuechange","tabview","array-extras"]},"moodle-atto_h5p-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_html-codemirror":{"requires":["moodle-atto_html-codemirror-skin"]},"moodle-atto_html-beautify":{},"moodle-atto_html-button":{"requires":["promise","moodle-editor_atto-plugin","moodle-atto_html-beautify","moodle-atto_html-codemirror","event-valuechange"]},"moodle-atto_image-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_indent-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_italic-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_link-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-usedfiles":{"requires":["node","escape"]},"moodle-atto_managefiles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_mb2shortcodes-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_media-button":{"requires":["moodle-editor_atto-plugin","moodle-form-shortforms"]},"moodle-atto_noautolink-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_orderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_recordrtc-button":{"requires":["moodle-editor_atto-plugin","moodle-atto_recordrtc-recording"]},"moodle-atto_recordrtc-recording":{"requires":["moodle-atto_recordrtc-button"]},"moodle-atto_rtl-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_strike-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_subscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_superscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_table-button":{"requires":["moodle-editor_atto-plugin","moodle-editor_atto-menu","event","event-valuechange"]},"moodle-atto_teamsmeeting-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_title-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_underline-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_undo-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_unorderedlist-button":{"requires":["moodle-editor_atto-plugin"]}}},"gallery":{"name":"gallery","base":"https:\/\/elearning.zetech.ac.ke\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/elearning.zetech.ac.ke\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1610711879\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/elearning.zetech.ac.ke\/lib\/javascript.php\/1610711879\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker","moodle-core-notification-dialogue"]},"core_comment":{"name":"core_comment","fullpath":"https:\/\/elearning.zetech.ac.ke\/lib\/javascript.php\/1610711879\/comment\/comment.js","requires":["base","io-base","node","json","yui2-animation","overlay","escape"]},"mathjax":{"name":"mathjax","fullpath":"https:\/\/cdn.jsdelivr.net\/npm\/mathjax@2.7.8\/MathJax.js?delayStartupUntil=configured"}}};
M.yui.loader = {modules: {}};

//]]>
</script>
	<script>(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');ga('create', 'UA-76472924-8', 'auto');ga('send', 'pageview');</script></head>
<body  id="page-site-index" class="format-site course path-site chrome dir-ltr lang-en yui-skin-sam yui3-skin-sam elearning-zetech-ac-ke pagelayout-frontpage course-1 context-2 notloggedin theme-lfw header-light coursetheme- sticky-nav bookmarks-enabled fpempty sidebar-case sidebar-one custom_id_a59e006be59d custom_id_5e37f615d176 custom_id_5b1649004a21">
<div>
    <a class="sr-only sr-only-focusable" href="#maincontent">Skip to main content</a>
</div><script src="https://elearning.zetech.ac.ke/lib/javascript.php/1610711879/lib/babel-polyfill/polyfill.min.js"></script>
<script src="https://elearning.zetech.ac.ke/lib/javascript.php/1610711879/lib/polyfills/polyfill.js"></script>
<script src="https://elearning.zetech.ac.ke/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js"></script><script src="https://elearning.zetech.ac.ke/theme/jquery.php/core/jquery-3.4.1.min.js"></script>
<script src="https://elearning.zetech.ac.ke/lib/javascript.php/1610711879/lib/javascript-static.js"></script>
<script>
//<![CDATA[
document.body.className += ' jsenabled';
//]]>
</script>

<div id="page-outer">
<div id="page">
<div id="page-a">
			<div id="top-panel">
	    	<div class="container-fluid">
	        	<div class="row">
	            	<div class="col-md-12">
	                    	                    						<div class="theme-usertools"><div class="theme-fontsizer"><span class="title">Font size:</span> <a class="fs1" href="#" data-size="1" title="Small font">A</a><a class="fs2" href="#" data-size="2" title="Medium font">A</a><a class="fs3" href="#" data-size="3" title="Big font">A</a></div></div>	        		</div>
	 			</div>
			</div>
	    </div>
	        	<div class="sticky-nav-element-offset"></div>
        <div id="main-header">
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-12">
                    <div class="main-logo" style="width:400px;margin-top:77;">
	<a href="https://elearning.zetech.ac.ke" title="Zetech Digital School">
		<img src="//elearning.zetech.ac.ke/pluginfile.php/1/theme_mb2iq/logo/1610721501/zetech%20digital%20school%20banner%2014-min.png" alt="Zetech Digital School">
	</a>                    
</div>
<div class="menu-bar">
	<a class="show-menu" href="#"><i class="fa fa-bars"></i></a>		
</div>
<div class="menu-clear clearfix"></div>                  	<div id="main-navigation">
                   		<div class="main-navigation-inner">
                       		<ul class="main-menu theme-ddmenu" data-animtype="2" data-animspeed="300" data-breakpoint="768"><li class=""><a class="" href="https://elearning.zetech.ac.ke/my/">My Courses</a></li><li class=""><a class="" href="https://elearning.zetech.ac.ke/course/view.php?id=13">News and Announcement</a></li><li class="dropdown"><a href="https://elearning.zetech.ac.ke/course/view.php?id=25" class="" data-toggle="">Learner Support<span class="mobile-arrow"></span></a><ul class="dropdown-list"><li class="dropdown"><a href="https://elearning.zetech.ac.ke/course/view.php?id=25" class="" data-toggle="">Learner Support Area<span class="mobile-arrow"></span></a><ul class="dropdown-list"><li class=""><a class="" href="https://elearning.zetech.ac.ke/course/view.php?id=28">Orientation to eLearning</a></li></ul><li class=""><a class="" href="https://elearning.zetech.ac.ke/course/view.php?id=20">Research Support</a></li><li class=""><a class="" href="https://portal.zetech.ac.ke">Student Portal</a></li><li class=""><a class="" href="https://elearning.zetech.ac.ke/course/view.php?id=24">FAQ</a></li></ul><li class=""><a class="" href="https://elearning.zetech.ac.ke/mod/page/view.php?id=4518">Our Contacts</a></li><li class=""><a class="" href="https://libraryzetech.remotexs.xyz/user/login"target="_blank">Library</a></li><li class="dropdown"><a href="#" class="" data-toggle="">Progression<span class="mobile-arrow"></span></a><ul class="dropdown-list"><li class=""><a class="" href="https://zetech.ac.ke/wp-content/uploads/2020/08/progression-path-zu.jpg"target="_blank">ZU Programme</a></li><li class=""><a class="" href="https://zetech.ac.ke/wp-content/uploads/2020/08/progression-path-knec.jpg"target="_blank">KNEC Programme</a></li></ul></ul>                     	</div>
                 	</div>
                </div>
            </div>
        </div>
    </div>
	    <div class="sliding-panel dark1 closed">
	<a href="#" class="close-panel">&times;</a>
	<div class="container-fluid">
		<div class="row">
			<div class="col-md-12 clearfix">
				<div class="theme-searchform"><form id="theme-search" action="https://elearning.zetech.ac.ke/course/search.php" method="get"><input id="theme-coursesearchbox" type="text" value="" placeholder="Search courses" name="search"><button type="submit"><i class="fa fa-search"></i></button></form></div>                <div class="theme-loginform" style="display:none;"><form id="header-form-login" method="post" action="https://elearning.zetech.ac.ke/login/index.php"><div class="form-field"><label id="user"><i class="fa fa-user"></i></label><input id="login-username" type="text" name="username" placeholder="Username" /></div><div class="form-field"><label id="pass"><i class="fa fa-lock"></i></label><input id="login-password" type="password" name="password" placeholder="Password" /></div><button type="submit"><i class="fa fa-angle-right"></i></button><input type="hidden" name="logintoken" value="BZBzQr8g89gBYxiehB1syaAQviDYwqYg" /></form><p class="login-info"><a href="https://elearning.zetech.ac.ke/login/index.php">Forgot your username or password?</a></p></div>                                <div class="header-tools"><div class="theme-plugins"></div><a href="#" class="panel-tool tool-search header-tool-js" title="Search courses"><i class="fa fa-search"></i><span class="text1">Search courses</span><span class="text2">Close</span></a><a href="#" class="panel-tool tool-login header-tool-js" title="Log in"><i class="fa fa-lock"></i><span class="text1">Log in</span><span class="text2">Close</span></a></div>			</div>
		</div>
	</div>
</div>
</div><!-- //end #page-a -->
<div id="page-b">
<div id="subheader">
		</div>
<div id="main-content" class="light">
<div class="section-inner"  style="padding-top:40px;padding-bottom:10px;">
    <div class="container-fluid">
        <div class="row">
            <div id="region-main" class="content-col col-md-9">
                <div id="page-content">
					                	<span class="notifications" id="user-notifications"></span>					                	<div role="main"><span id="maincontent"></span><div class="box py-3 generalbox sitetopic"><div class="no-overflow"><div class="theme-boxes theme-col-4 gutter-normal clearfix"><div class="theme-box"><div class="theme-boxcontent type-2 color-primary isicon"><div class="theme-boxcontent-content"><div class="theme-boxcontent-icon"><i class="fa fa-user"></i></div><h4><div class="text_to_html">My Courses</div></h4><div class="text_to_html">Access your Courses and timeline from this Link.<br />
<br />
</div></div></div></div><div class="theme-box"><div class="theme-boxcontent type-2 color-primary isicon"><div class="theme-boxcontent-content"><div class="theme-boxcontent-icon"><i class="fa fa-bullhorn"></i></div><h4><div class="text_to_html">News and Announcement</div></h4><div class="text_to_html">Get to know what is happening at ZDS</div></div></div></div><div class="theme-box"><div class="theme-boxcontent type-2 color-primary isicon"><div class="theme-boxcontent-content"><div class="theme-boxcontent-icon"><i class="fa fa-users"></i></div><h4><div class="text_to_html">Getting Started </div></h4><div class="text_to_html">Learn how to navigate and use the site tools</div></div></div></div><div class="theme-box"><div class="theme-boxcontent type-2 color-primary isicon"><div class="theme-boxcontent-content"><div class="theme-boxcontent-icon"><i class="fa fa-smile-o"></i></div><h4><div class="text_to_html">FAQs</div></h4><div class="text_to_html">Get to know more about eLearning at Zetech University<br />
<br />
</div></div></div></div></div></div><ul class="section img-text"></ul></div><br /></div>                                                        	                </div>
            </div>
     		            	<div class="sidebar-col col-md-3">
                	<aside id="block-region-side-pre" class="side-pre style-default block-region" data-blockregion="side-pre" data-droptarget="1"><a href="#sb-1" class="sr-only sr-only-focusable">Skip Navigation</a>

<section id="inst20"
     class=" block_navigation block  card mb-3"
     role="navigation"
     data-block="navigation"
          aria-labelledby="instance-20-header"
     >

    <div class="card-body p-3">

            <h5 id="instance-20-header" class="card-title d-inline">Navigation</h5>


        <div class="card-text content mt-3">
            <ul class="block_tree list" role="tree" data-ajax-loader="block_navigation/nav_loader"><li class="type_unknown depth_1 contains_branch current_branch" aria-labelledby="label_1_1"><p class="tree_item branch active_tree_node canexpand navigation_node" role="treeitem" aria-expanded="true" aria-owns="random601a97f41d3331_group" data-collapsible="false"><a tabindex="-1" id="label_1_1" href="https://elearning.zetech.ac.ke/">Home</a></p><ul id="random601a97f41d3331_group" role="group"><li class="type_system depth_2 contains_branch" aria-labelledby="label_2_3"><p class="tree_item branch" role="treeitem" id="expandable_branch_0_courses" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_0_courses" data-node-key="courses" data-node-type="0"><a tabindex="-1" id="label_2_3" href="https://elearning.zetech.ac.ke/course/index.php">Courses</a></p></li></ul></li></ul>
            <div class="footer"></div>
            
        </div>

    </div>

</section>

  <span id="sb-1"></span></aside>                </div>
       		     		        </div>
    </div>
</div>
</div>
<div id="bottom-info">
	<div class="container-fluid">
   		<div class="row">
       		<div class="col-md-12">
       			             	         	</div>
 		</div>
	</div>
    <span class="bar"></span>
</div>
<footer id="footer">
	<div class="container-fluid">
    	<div class="row">
        	<div class="col-md-4">
				<p class="footer-text">Copyright © Zetech University 2021. All rights reserved.</p>
           	</div>
      		        </div>
    </div>
	</footer>
</div><!-- //end #page-b -->
</div><!-- //end #page -->
</div><!-- //end #page-outer -->
<ul class="theme-static-content theme-iconnav"><li class="theme-static-item1"><a class="link-replace" href="http://https://zetech.ac.ke/"><span class="static-icon"><i class="fa fa-life-ring"></i></span><span class="text">Zetech University Website</span></a></li><li class="theme-static-item2"><a class="link-replace" href="https://zetech.ac.ke/type/degree/"><span class="static-icon"><i class="fa fa-link"></i></span><span class="text">Our Programmes</span></a></li><li class="theme-static-item3"><a class="link-replace" href="https://zds.zetech.ac.ke/mod/page/view.php?id=36519"><span class="static-icon"><i class="fa fa-flag"></i></span><span class="text">Get Help 0714588863</span></a></li></ul><div class="fixed-bar">
		<a href="#" class="theme-hide-sidebar mode1" data-showtext="Show sidebars" data-hidetext="Hide sidebars">Hide sidebars</a></div>
<script>
//<![CDATA[
var require = {
    baseUrl : 'https://elearning.zetech.ac.ke/lib/requirejs.php/1610711879/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,
    waitSeconds : 0,

    paths: {
        jquery: 'https://elearning.zetech.ac.ke/lib/javascript.php/1610711879/lib/jquery/jquery-3.4.1.min',
        jqueryui: 'https://elearning.zetech.ac.ke/lib/javascript.php/1610711879/lib/jquery/ui-1.12.1/jquery-ui.min',
        jqueryprivate: 'https://elearning.zetech.ac.ke/lib/javascript.php/1610711879/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },
      // Stub module for 'process'. This is a workaround for a bug in MathJax (see MDL-60458).
      '*': { process: 'core/first' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
</script>
<script src="https://elearning.zetech.ac.ke/lib/javascript.php/1610711879/lib/requirejs/require.min.js"></script>
<script>
//<![CDATA[
M.util.js_pending("core/first");require(['core/first'], function() {
require(['core/prefetch']);
;
require(["media_videojs/loader"], function(loader) {
    loader.setUp('en');
});;
M.util.js_pending('block_navigation/navblock'); require(['block_navigation/navblock'], function(amd) {amd.init("20"); M.util.js_complete('block_navigation/navblock');});;
M.util.js_pending('block_settings/settingsblock'); require(['block_settings/settingsblock'], function(amd) {amd.init("21", null); M.util.js_complete('block_settings/settingsblock');});;
require(['theme_boost/loader']);require(['jquery','theme_boost/bootstrap/index'], function($){$('[data-toggle="tooltip"]').tooltip();$('[data-toggle="popover"]').popover()});;
M.util.js_pending('core/notification'); require(['core/notification'], function(amd) {amd.init(2, []); M.util.js_complete('core/notification');});;
M.util.js_pending('core/log'); require(['core/log'], function(amd) {amd.setConfig({"level":"warn"}); M.util.js_complete('core/log');});;
M.util.js_pending('core/page_global'); require(['core/page_global'], function(amd) {amd.init(); M.util.js_complete('core/page_global');});M.util.js_complete("core/first");
});
//]]>
</script>
<script src="https://elearning.zetech.ac.ke/lib/javascript.php/1610711879/theme/mb2iq/assets/superfish/superfish.custom.js"></script>
<script src="https://elearning.zetech.ac.ke/lib/javascript.php/1610711879/theme/mb2iq/assets/lightslider/lightslider.custom.min.js"></script>
<script src="https://elearning.zetech.ac.ke/lib/javascript.php/1610711879/theme/mb2iq/assets/OwlCarousel/owl.carousel.min.js"></script>
<script src="https://elearning.zetech.ac.ke/lib/javascript.php/1610711879/theme/mb2iq/assets/js.cookie.js"></script>
<script src="https://elearning.zetech.ac.ke/lib/javascript.php/1610711879/theme/mb2iq/javascript/theme.js"></script>
<script src="https://elearning.zetech.ac.ke/lib/javascript.php/1610711879/theme/mb2iq/assets/youtube/player_api.js"></script>
<script>
//<![CDATA[
M.str = {"moodle":{"lastmodified":"Last modified","name":"Name","error":"Error","info":"Information","yes":"Yes","no":"No","viewallcourses":"View all courses","cancel":"Cancel","morehelp":"More help","loadinghelp":"Loading...","confirm":"Confirm","areyousure":"Are you sure?","closebuttontitle":"Close","unknownerror":"Unknown error","file":"File","url":"URL"},"repository":{"type":"Type","size":"Size","invalidjson":"Invalid JSON string","nofilesattached":"No files attached","filepicker":"File picker","logout":"Logout","nofilesavailable":"No files available","norepositoriesavailable":"Sorry, none of your current repositories can return files in the required format.","fileexistsdialogheader":"File exists","fileexistsdialog_editor":"A file with that name has already been attached to the text you are editing.","fileexistsdialog_filemanager":"A file with that name has already been attached","renameto":"Rename to \"{$a}\"","referencesexist":"There are {$a} alias\/shortcut files that use this file as their source","select":"Select"},"admin":{"confirmdeletecomments":"You are about to delete comments, are you sure?","confirmation":"Confirmation"},"debug":{"debuginfo":"Debug info","line":"Line","stacktrace":"Stack trace"},"langconfig":{"labelsep":": "}};
//]]>
</script>
<script>
//<![CDATA[
(function() {Y.use("moodle-filter_mathjaxloader-loader",function() {M.filter_mathjaxloader.configure({"mathjaxconfig":"\nMathJax.Hub.Config({\n    config: [\"Accessible.js\", \"Safe.js\"],\n    errorSettings: { message: [\"!\"] },\n    skipStartupTypeset: true,\n    messageStyle: \"none\"\n});\n","lang":"en"});
});
M.util.help_popups.setup(Y);
Y.use("moodle-core-popuphelp",function() {M.core.init_popuphelp();
});
 M.util.js_pending('random601a97f41d3333'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random601a97f41d3333'); });
})();
//]]>
</script>
</body>
</html>
