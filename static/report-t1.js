/**
 * Created by Administrator on 2016/9/28.
 */


// 医疗统计信息
function TreatmentInformation_pie() {

var data = document.getElementById('dataid').getAttribute('d');
    var arr = data.split(";")
    var key = new Array();
    var value = new Array()
    for(var i = 0 ; i < arr.length ; i++ ){

        if(i%2 == 0){
            key .push(arr[i])
        }else {
            value .push(parseInt(arr[i]))
        }
    }


    Highcharts.theme = {
         colors: ['#000000', '#000000', '#000000', '#f7a35c', '#8085e9', '#f15c80', '#e4d354', '#8085e8', '#8d4653', '#91e8e1'],
        chart: {
            className: 'skies',
            borderWidth: 0,
            plotShadow: true,
            plotBackgroundImage: 'http://www.highcharts.com/demo/gfx/skies.jpg',
            plotBackgroundColor: {
                linearGradient: [0, 0, 250, 500],
                stops: [
                    [0, 'rgba(255, 255, 255, 1)'],
                    [1, 'rgba(255, 255, 255, 0)']
                ]
            },
            plotBorderWidth: 1
        },
        title: {
            style: {
                color: '#3E576F',
                font: '16px Lucida Grande, Lucida Sans Unicode, Verdana, Arial, Helvetica, sans-serif'
            }
        },
        subtitle: {
            style: {
                color: '#6D869F',
                font: '12px Lucida Grande, Lucida Sans Unicode, Verdana, Arial, Helvetica, sans-serif'
            }
        },
        xAxis: {
            gridLineWidth: 0,
            lineColor: '#C0D0E0',
            tickColor: '#C0D0E0',
            labels: {
                style: {
                    color: '#666',
                    fontWeight: 'bold'
                }
            },
            title: {
                style: {
                    color: '#666',
                    font: '12px Lucida Grande, Lucida Sans Unicode, Verdana, Arial, Helvetica, sans-serif'
                }
            }
        },
        yAxis: {
            alternateGridColor: 'rgba(255, 255, 255, .5)',
            lineColor: '#C0D0E0',
            tickColor: '#C0D0E0',
            tickWidth: 1,
            labels: {
                style: {
                    color: '#666',
                    fontWeight: 'bold'
                }
            },
            title: {
                style: {
                    color: '#666',
                    font: '12px Lucida Grande, Lucida Sans Unicode, Verdana, Arial, Helvetica, sans-serif'
                }
            }
        },
        legend: {
            itemStyle: {
                font: '9pt Trebuchet MS, Verdana, sans-serif',
                color: '#3E576F'
            },
            itemHoverStyle: {
                color: 'black'
            },
            itemHiddenStyle: {
                color: 'silver'
            }
        },
        labels: {
            style: {
                color: '#3E576F'
            }
        }
    };

// Apply the theme
    var highchartsOptions = Highcharts.setOptions(Highcharts.theme);


    Highcharts.getOptions().colors = Highcharts.map(Highcharts.getOptions().colors, function (color) {
        return {
            radialGradient: {cx: 0.5, cy: 0.3, r: 0.7},
            stops: [
                [0, color],
                [1, Highcharts.Color(color).brighten(-0.3).get('rgb')] // darken
            ]
        };
    });
    $('#TreatmentInformation_pie').highcharts({
            colors: ['#000000', '#000000', '#000000', '#f7a35c', '#8085e9', '#f15c80', '#e4d354', '#8085e8', '#8d4653', '#91e8e1'],
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: '治疗信息 统计图'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    color: '#000000',
                    connectorColor: '#000000',
                    formatter: function () {
                        return '<b>' + this.point.name + '</b>: ' + this.point.y + ' 次';
                    }
                }
            }
        },
        series: [{
            type: 'pie',
            name: 'Browser share',
            data: [

                    [key[1],value[1]],
                    [key[2],value[2]],
                    [key[3],value[3]],
                   {
                    name:key[0] ,
                    y: value[0] ,
                    sliced: true,
                    selected: true
                    },
                    [key[4],value[4]],
                    [key[5],value[5]],
                    [key[6],value[6]],
            ]
        }]
    });
}
