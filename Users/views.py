# Importing Libraries
from .models import UserHappiness, Users, Teams
from rest_framework import viewsets
from .serializers import usersSerializer
from rest_framework.response import Response
from rest_framework import status
from .filters import UserFilterSet
from django.http import JsonResponse
from rest_framework.decorators import api_view
from numpy import mean


class UsersView(viewsets.ModelViewSet):
    queryset = UserHappiness.objects.all()
    serializer_class = usersSerializer
    filterset_class = UserFilterSet

    def perform_create(self, serializer):
        request_data = serializer.data
        username = request_data['username']
        happiness_date = request_data['happiness_date']
        if UserHappiness.objects.filter(username=username, happiness_date=happiness_date).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = usersSerializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    team_id = UserHappiness.objects.filter(username_id = pk).values_list('username__userteam_id', flat=True).distinct()
    if not team_id:
        dic = {"average_all_teams": mean(UserHappiness.objects.values_list('happiness_level', flat=True))}
    else:
        all_team_users = Users.objects.filter(userteam__in=team_id).values_list('username',flat=True)
        happiness_levels = []
        for user in all_team_users:
            happiness = UserHappiness.objects.filter(username__username=user, username__userteam__in=team_id)
            happiness_level = list(happiness.values("happiness_level"))
            happiness_value = 0.0
            for h in happiness_level:
                happiness_value += h['happiness_level']
            happiness_levels.append(happiness_value)
        average_happiness = 0.0
        datalist = []
        for i in range(len(all_team_users)):
            dic = {'username': all_team_users[i], 'happiness_level': happiness_levels[i]}
            average_happiness += happiness_levels[i]
            datalist.append(dic)
        average_happiness = average_happiness / len(all_team_users)
        dic = {"results": datalist, "average_team_happiness": average_happiness}
    return JsonResponse(dic)