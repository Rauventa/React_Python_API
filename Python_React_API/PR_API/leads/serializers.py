from rest_framework import serializers
from leads.models import Lead


# Lead serializers

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
