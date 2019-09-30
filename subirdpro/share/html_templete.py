# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-09-17 17:53:20
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-09-17 17:53:20
'''
import time

class TestTemplate(object):
    """
    Define a HTML template for report customerization and generation.

    Overall structure of an HTML report

    HTML
    +------------------------+
    |<html>                  |
    |  <head>                |
    |                        |
    |   STYLESHEET           |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </head>               |
    |                        |
    |  <body>                |
    |                        |
    |   DASHBOARD HEADER     |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   DASHBOARD            |
    |   +-------+ +-------+  |
    |   |       | |       |  |
    |   +-------+ +-------+  |
    |                        |
    |   DETAIL               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </body>               |
    |</html>                 |
    +------------------------+
    """

    LAN = {
        0: 'CN',
        1: 'EN',
    }

    STATUS = {
        "CN":{
            "Success":'通过',
            "Failure": '失败',
            "Skip": '跳过',
            "Error": '错误',
        },
        "EN":{
            "Success":'Success',
            "Failure": 'Failure',
            "Skip": 'Skip',
            "Error": 'Error',
        }
    }

    DEFAULT_TEST_NAME = time.strftime("%Y%m%d%H%M%S")
    DEFAULT_DESCRIPTION = ''
    DEFAULT_TESTER = {"CN":"最棒测试", "EN":"Best QA"}

    LABEL_HTML = {
        "CN":{
            "TitlePage":"单元测试报告",
            "TitleReport": "测试报告",
            "TitleSummary": "测试汇总",
            "TitleDetail": "测试详情",
        },
        "EN":{
            "TitlePage":"Unit Test Report",
            "TitleReport": "Test Report",
            "TitleSummary": "Test Summary",
            "TitleDetail": "Test Detail",
        },
    }

    LABEL_DETAIL_HEADER = {
        "CN":{
            "ClassFilter":"-----测试类筛选-----",
            "ResultFilter":"--测试结果筛选--",
            "TotalCount":"总数",
        },
        "EN":{
            "ClassFilter":"----Class Filter----",
            "ResultFilter":"--Result Filter--",
            "TotalCount":"Total",
        }
    }

    LABEL_DETAIL_BODY = {
        "CN":{
            "TestId":"编号",
            "TestClass":"类别",
            "TestMethod":"方法",
            "TestDesc":"描述",
            "TestSTime":"耗时",
            "TestResult":"结果",
            "Operation":"操作",
        },
        "EN":{
            "TestId":"Id",
            "TestClass":"Class",
            "TestMethod":"Method",
            "TestDesc":"Description",
            "TestSTime":"Spend Time",
            "TestResult":"Result",
            "Operation":"Operation",
        }
    }

    LABEL_SUMMARY = {
        "CN":{
            "TestName":"测试名称",
            "TestCount":"测试总数",
            "TestSuccess":"测试通过",
            "TestFailure":"测试失败",
            "TestSkip":"测试跳过",
            "TestError":"测试错误",
            "TestBegin":"开始时间",
            "TestSpend":"运行时间",
        },
        "EN":{
            "TestName":"Test Name",
            "TestCount":"Test Count",
            "TestSuccess":"Test Success",
            "TestFailure":"Test Failure",
            "TestSkip":"Test Skip",
            "TestError":"Test Error",
            "TestBegin":"Test Begin",
            "TestSpend":"Test Spend",
        }
    }



    HTML_DETAIL_BODY = r"""
    <table class="table table-bordered">
        <thead>
            <tr>
                <th>%(test_id)s</th>
                <th>%(test_class)s</th>
                <th>%(test_method)s</th>
                <th>%(test_desc)s</th>
                <th>%(test_stime)s</th>
                <th>%(test_result)s</th>
                <th>%(test_operation)s</th>
            </tr>
        </thead>
        <tbody id="detail_body">
        </tbody>
    </table>
    """

    HTML_DETAIL_HEADER = r"""
    <div class="input-group panel-heading">
        <select class="chosen-select form-control" style="width:300px; background-color:#f3f3f4" name="filterClass"
            id="filterClass">
            <option value="">%(class_filter)s</option>
        </select>
        <select class="chosen-select form-control" style="width:150px; background-color:#f3f3f4" name="filterResult"
            id="filterResult">
            <option value="">%(result_filter)s</option>
        </select>
        <div style="float: right">
            <label class="form-control" style="background-color:#f3f3f4">
                <span class="text-navy">%(total_count)s: </span><span class="text-navy b-r" id="filter_all"></span><span>
                    | </span>
                <span class="text-success">%(success_count)s: </span><span class="text-success" id="filter_ok"></span><span>
                    | </span>
                <span class="text-danger">%(fail_count)s: </span><span class="text-danger" id="filter_fail"></span><span>
                    | </span>
                <span class="text-danger">%(error_count)s: </span><span class="text-danger" id="filter_error"></span><span>
                    | </span>
                <span class="text-warning">%(skip_count)s: </span><span class="text-warning" id="filter_skip"></span>
            </label>
        </div>
    </div>
    """

    HTML_SUMMARY = r"""
    <form class="form-horizontal">
        <div class="form-group">
            <label class="col-sm-4 control-label text-navy">%(test_name)s:</label>
            <label class="col-sm-4 text-navy label-show" id="test_name"></label>
        </div>
        <div class="form-group">
            <label class="col-sm-4 control-label text-navy">%(test_count)s:</label>
            <label class="col-sm-4 text-navy label-show" id="test_all">0</label>
        </div>
        <div class="form-group">
            <label class="col-sm-4 control-label text-success">%(test_success)s:</label>
            <label class="col-sm-4 text-success label-show" id="test_pass">0</label>
        </div>
        <div class="form-group">
            <label class="col-sm-4 control-label text-danger">%(test_failure)s:</label>
            <label class="col-sm-4 text-danger label-show" id="test_fail">0</label>
        </div>
        <div class="form-group">
            <label class="col-sm-4 control-label text-danger">%(test_error)s:</label>
            <label class="col-sm-4 text-danger label-show" id="test_error">0</label>
        </div>
        <div class="form-group">
            <label class="col-sm-4 control-label text-warning">%(test_skip)s:</label>
            <label class="col-sm-4 text-warning label-show" id="test_skip">0</label>
        </div>
        <div class="form-group">
            <label class="col-sm-4 control-label text-navy">%(test_begin)s:</label>
            <label class="col-sm-4 text-navy label-show" id="begin_time">0000-00-00 00:00:00</label>
        </div>
        <div class="form-group">
            <label class="col-sm-4 control-label text-navy">%(test_spend)s:</label>
            <label class="col-sm-4 text-navy label-show" id="run_time">0s</label>
        </div>
    </form>
    """
    LABEL_SCRIPT = {
        "CN":{
            "LabelShow":"展开",
            "LabelHidden":"收起",
            "TitleEchart":"测试运行结果",
        },
        "EN":{
            "LabelShow":"Show",
            "LabelHidden":"Hidden",
            "TitleEchart":"Test Result",
        },
    }
    HTML_TEMP = r"""
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>%(title_page)s</title>

        <link href="https://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdn.bootcss.com/chosen/1.8.2/chosen.css" rel="stylesheet">
        <script src="https://cdn.bootcss.com/jquery/2.1.4/jquery.min.js"></script>
        <script src="https://cdn.bootcss.com/echarts/3.8.5/echarts.min.js"></script>
        <script src="https://cdn.bootcss.com/chosen/1.8.2/chosen.jquery.js"></script>
        <style type="text/css">
            %(temp_css)s
        </style>
        <script type="text/javascript">
            var resultData = %(result_data)s;
            var labelShow = '%(label_show)s';
            var labelHidden = '%(label_hidden)s';
            var titleEchart = '%(title_echart)s';
            var labelSuccess = '%(label_success)s';
            var labelFailure = '%(label_failure)s';
            var labelError = '%(label_error)s';
            var labelSkip = '%(label_skip)s';
            %(temp_script)s
        </script>
    </head>

    <body class="gray-bg">
        <div class="row dashboard-header">
            <div class="col-sm-12 text-center">
                <span class="header-font">%(title_report)s</span>
            </div>
        </div>
        <div class="row dashboard">
            <div class="col-sm-12 ibox">
                <div class="ibox-title">
                    <h5>%(title_summary)s</h5>
                </div>
                <div class="row ibox-content">
                    <div class="col-sm-6 no-padding">%(temp_summary)s</div>
                    <div class="col-sm-6">
                        <div style="height:350px" id="echarts-map-chart"></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row dashboard">
            <div class="col-sm-12">
                <div class="ibox">
                    <div class="ibox-title">
                        <h5>%(title_detail)s</h5>
                    </div>
                    <div class="ibox-content">
                        %(temp_detail_header)s
                        %(temp_detail_body)s
                    </div>
                </div>
            </div>
        </div>
        </div>
    </body>
    </html>
    """

    CSS = r"""
        .dashboard-header {
            border-top: 0;
            padding: 20px;
            background-color: #1ab394;
        }

        .row {
            margin-left: 20px;
            margin-right: 20px;
        }

        .header-font {
            color: #ffffff;
            font-size: 30px;
            font-weight: 700;
        }

        .gray-bg {
            background-color: #f3f3f4
        }

        .dashboard {
            padding-top: 10px;
            margin-top: 20px;
            color: #676a6c;
            background-color: #e4e4e4;
            box-shadow: 0px -3px 8px 3px rgba(0, 0, 0, 0.3);
        }

        .ibox-title {
            border-color: #969696;
            border-style: solid solid solid;
            border-width: 0px 0px 1px;
            min-height: 50px;
            padding: 15px 0px 0px;
        }

        .ibox-title h5 {
            display: inline-block;
            font-size: 20px;
            font-weight: 600;
            margin: 0 0 7px;
            padding: 0;
            color: inherit
        }

        .ibox-content {
            padding-bottom: 0;
            padding-top: 15px
        }

        .no-padding {
            padding-left: 0px;
            padding-right: 0px
        }

        .label-show {
            float: left;
            padding-top: 7px;
            font-weight: 400;
        }

        .input-group {
            width: 100%;
            background-color: #1ab394;
            margin-bottom: 10px;
            text-align: left;
            font-family: Consolas;
        }
    """

    SCRIPT = r"""
    function details(obj) {
        if ($(obj).text() == labelShow) {
            var len = $(obj).parent().parent().children().length;
            var detailLog = "";
            var logs = resultData["testResult"][parseInt($(obj).attr("buttonIndex"))]["log"];
            $(obj).text(labelHidden);
            $(obj).removeClass("btn-primary");
            $(obj).addClass("btn-danger");
            detailLog = "<p>" + logs + "</p>";
            $(obj).parent().parent().after("<tr><td colspan='" + len + "'><div style='font-family: Consolas;font-size:12px'>" + detailLog + "</div></td></tr>");
        } else if ($(obj).text() == labelHidden) {
            $(obj).parent().parent().next().remove();
            $(obj).text(labelShow);
            $(obj).removeClass("btn-danger");
            $(obj).addClass("btn-primary");
        }
    }

    $(function() {
        $("#test_name").text(resultData["testName"]);
        $("#test_pass").text(resultData["testPass"]);
        $("#test_fail").text(resultData["testFail"]);
        $("#test_error").text(resultData["testError"]);
        $("#test_skip").text(resultData["testSkip"]);
        $("#test_all").text(resultData["testAll"]);
        $("#begin_time").text(resultData["beginTime"]);
        $("#run_time").text(resultData["totalTime"]);
        $("#filter_all").text(resultData["testAll"]);
        $("#filter_ok").text(resultData["testPass"]);
        $("#filter_fail").text(resultData["testFail"]);
        $("#filter_skip").text(resultData["testSkip"]);
        $("#filter_error").text(resultData["testError"]);
        var classNames = [];
        var results = [];
        $.each(resultData["testResult"],
        function(i, n) {
            if (classNames.indexOf(n["className"]) == -1) {
                classNames.push(n["className"]);
            }
            if (results.indexOf(n["status"]) == -1) {
                results.push(n["status"]);
            }
        });

        $.each(classNames,
        function(i, n) {
            $("#filterClass").append("<option value='" + n + "' hassubinfo='true'>" + n + "</option>");
        });
        $.each(results,
        function(i, n) {
            $("#filterResult").append("<option value='" + n + "' hassubinfo='true'>" + n + "</option>");
        });

        $("#filterClass").chosen({
            search_contains: true
        });
        $("#filterResult").chosen({
            search_contains: true
        });

        function generateResult(className, caseResult) {
            $("#detail_body").children().remove();
            var filterAll = 0;
            var filterOk = 0;
            var filterFail = 0;
            var filterSkip = 0;
            var filterError = 0;

            $.each(resultData["testResult"],
            function(i, n) {
                if ((className == "" || n["className"] == className) && (caseResult == "" || n["status"] == caseResult)) {
                    filterAll += 1;
                    var status = "";
                    if (n["status"] == labelSuccess) {
                        filterOk += 1;
                        status = "<td><span class='text-success'>"+ labelSuccess +"</span></td>";
                    } else if (n["status"] == labelFailure) {
                        filterFail += 1;
                        status = "<td><span class='text-danger'>"+ labelFailure +"</span></td>";
                    } else if (n["status"] == labelSkip) {
                        filterSkip += 1;
                        status = "<td><span class='text-warning'>"+ labelSkip +"</span></td>";
                    } else if (n["status"] == labelError) {
                        filterError += 1;
                        status = "<td><span class='text-danger'>"+ labelError +"</span></td>";
                    } else {
                        status = "<td><span>" + n["status"] + "</span></td>";
                    }
                    var tr = "<tr style='font-family: Consolas'>" + "<td>" + (i + 1) + "</td>" + "<td>" + n["className"] + "</td>" + "<td>" + n["methodName"] + "</td>" + "<td>" + n["description"] + "</td>" + "<td>" + n["spendTime"] + "ms</td>" + status + "<td><button type='button' onclick='details(this)' buttonIndex='" + i + "' class='btn btn-primary btn-xs' style='margin-bottom: 0px'>"+labelShow+"</button></td></tr>";
                    $("#detail_body").append(tr);
                }
            });
            $("#filter_all").text(filterAll);
            $("#filter_ok").text(filterOk);
            $("#filter_fail").text(filterFail);
            $("#filter_skip").text(filterSkip);
            $("#filter_error").text(filterError);
        }

        generateResult("", "");

        $("#filterClass").on('change',
        function() {
            var className = $("#filterClass").val();
            var caseResult = $("#filterResult").val();
            generateResult(className, caseResult);
        });

        $("#filterResult").on('change',
        function() {
            var className = $("#filterClass").val();
            var caseResult = $("#filterResult").val();
            generateResult(className, caseResult);
        });

        function pie() {
            var option = {
                title: {
                    text: titleEchart,
                    subtext: '',
                    x: 'center'
                },
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                color: ['#ff5722', '#ffb800', '#1ab394', '#a52a2a'],
                legend: {
                    orient: 'vertical',
                    left: 'left',
                    data: [labelFailure, labelSkip, labelSuccess, labelError]
                },
                series: [{
                    name: titleEchart,
                    type: 'pie',
                    radius: '55%',
                    center: ['50%', '60%'],
                    data: [{
                        value: resultData["testFail"],
                        name: labelFailure
                    },
                    {
                        value: resultData["testSkip"],
                        name: labelSkip
                    },
                    {
                        value: resultData["testPass"],
                        name: labelSuccess
                    },
                    {
                        value: resultData["testError"],
                        name: labelError
                    }],
                    itemStyle: {
                        emphasis: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }]
            };
            var chart = echarts.init(document.getElementById("echarts-map-chart"));
            chart.setOption(option);
        }

        pie();
    });
    """