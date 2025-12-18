from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Customer, ScheduleBulkMessage, MessageTemplate
from rest_framework.parsers import MultiPartParser, FormParser
import csv
import io
# Create your views here.
class CreateScheduledCampaignAPI(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):

        # 1. Template ID
        template_id = request.data.get("template_id")
        scheduled_time = request.data.get("scheduled_time")
        csv_file = request.FILES.get("file")

        if not template_id or not scheduled_time or not csv_file:
            return Response({"error": "template_id, scheduled_time and file are required"}, status=400)

        # 2. Template fetch
        try:
            template = MessageTemplate.objects.get(id=template_id, user=request.user)
        except:
            return Response({"error": "Template not found"}, status=404)

        # 3. Create campaign
        campaign = ScheduleBulkMessage.objects.create(
            user=request.user,
            template=template,
            scheduled_time=scheduled_time,
        )

        # 4. Read CSV
        decoded = csv_file.read().decode("utf-8").splitlines()
        reader = csv.DictReader(decoded)

        for row in reader:
            name = row.get("name")
            phone = row.get("phone")
            fee = row.get("fee", 0)

            # 5. Create or get customer
            customer, created = Customer.objects.get_or_create(
                user=request.user,
                phone_number=phone,
                defaults={"name": name, "fee": fee}
            )

            # 6. Add to campaign
            campaign.customers.add(customer)

        return Response({
            "message": "Scheduled Campaign Created Successfully",
            "campaign_id": campaign.id
        }, status=201)
