import random
import string
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import *
from django.db.models import Sum
@xframe_options_exempt
def dashboard(request, sub_id="", per_page=""):
    user_name = "DJBuser" + ''.join(random.choices(string.ascii_letters, k=10)) + "_" + str(sub_id)
    return render(request, 'DJBFiltration/templates/dashboard.html', {'per_page': str(per_page), 'sub_id': str(sub_id), 'user_name': user_name})


class AltogetherView(APIView):   
    
    @csrf_exempt
    def get_total_runtime(request):
        if request.method == 'POST':
            device_id = request.POST.get('device_id')
            sub_id = request.POST.get('sub_id')
            if device_id:
                total_runtime = RuntimeDetail.objects.filter(subscriberid=sub_id, metergroupid=device_id).aggregate(total_runtime=Sum('runtime'))
                time_cat = list(TimeCat.objects.filter(subscriberid=sub_id, metergroupid=device_id).values('time', 'status'))
                if time_cat:
                    response_data = {
                        'total_runtime': total_runtime['total_runtime'],
                    }
                    for i in range(min(4, len(time_cat))):
                        response_data[f'time{i + 1}'] = time_cat[i]['time']
                        response_data[f'status{i + 1}'] = time_cat[i]['status']
                    return JsonResponse(response_data)
                else:
                    return JsonResponse({'error': 'Device not found'}, status=404)
        return JsonResponse({'error': 'Invalid request'}, status=400)

    @method_decorator(xframe_options_exempt)
    def get(self, request, sub_id=""):
        meter_map = {}
        mapping_set = Metermap.objects.filter(subscriberid=sub_id).values('metergroupid', 'metergroupname')
        for item in mapping_set:
            meter_map[item['metergroupid']] = item['metergroupname']        
        def convert_minutes_to_dhm(minutes):
                minutes=int(minutes)
                days = minutes // 1440
                hours = (minutes % 1440) // 60
                mins = minutes % 60
                return f"{days} days, {hours} hours, {mins}"        
        maxrun = Maxruntime.objects.filter(subscriberid=sub_id).values('opening_datetime', 'closing_datetime', 'metergroupid', 'duration','status')
        maxrun_list = []
        for run in maxrun:
            duration_dhm = convert_minutes_to_dhm(run['duration'])
            opening_datetime = run['opening_datetime'].strftime('%Y -%m-%d %I:%M %p')
            closing_datetime = run['closing_datetime'].strftime('%Y -%m-%d %I:%M %p')
            run_data = {
                'opening_datetime': opening_datetime,
                'closing_datetime': closing_datetime,
                'metergroupname': meter_map.get(run['metergroupid'], ''),
                'duration': duration_dhm,
                'status' : run['status'],
            }
            maxrun_list.append(run_data)
        minrun = Minruntime.objects.filter(subscriberid=sub_id).values('opening_datetime', 'closing_datetime', 'metergroupid', 'duration','status')
        minrun_list = []
        for run in minrun:
            duration_dhm = convert_minutes_to_dhm(run['duration'])
            opening_datetime = run['opening_datetime'].strftime('%Y -%m-%d %I:%M %p')
            closing_datetime = run['closing_datetime'].strftime('%Y -%m-%d %I:%M %p')
            run_data = {
                'opening_datetime': opening_datetime,
                'closing_datetime': closing_datetime,
                'metergroupname': meter_map.get(run['metergroupid'], ''),
                'duration': duration_dhm,
                'status' : run['status'],
            }
            minrun_list.append(run_data)
        purest = Purest.objects.filter(subscriberid=sub_id).values('metergroupid')
        purest_list = []
        for pure in purest:
            pure_data = {
                'metergroupname': meter_map.get(pure['metergroupid'], ''),
            }
            purest_list.append(pure_data)
        impurest = Impurest.objects.filter(subscriberid=sub_id).values('metergroupid')
        impurest_list = []
        for impure in impurest:
            impure_data = {
                'metergroupname': meter_map.get(impure['metergroupid'], ''),

            }
            impurest_list.append(impure_data)
        context = {
            'sub_id': sub_id,
            'meter_map': meter_map,
            'user_name': "DJBuser" + ''.join(random.choices(string.ascii_letters, k=10)) + "_" + str(sub_id),
            'maxrun': maxrun_list,
            'minrun': minrun_list,
            'purest': purest_list,
            'impurest': impurest_list,
            'runtime_per_status': list(RuntimeDetail.objects.filter(subscriberid=sub_id).values('status').annotate(total_runtime=Sum('runtime')).order_by('status')),
            'changes_per_status': list(Statuschange.objects.filter(subscriberid=sub_id).values('status').annotate(total_changes=Sum('changes')).order_by('status')),
        }
        return render(request, 'DJBFiltration/templates/report.html', context)





