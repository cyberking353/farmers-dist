from django.shortcuts import render


from django.shortcuts import render, redirect, get_object_or_404
from .models import Farm
from .forms import FarmForm

def farm_list(request):
    farms = Farm.objects.all()
    return render(request, "farms/farm_list.html", {"farms": farms})

def farm_create(request):
    if request.method == "POST":
        form = FarmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("farm_list")
    else:
        form = FarmForm()
    return render(request, "farms/farm_form.html", {"form": form})

def farm_update(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    if request.method == "POST":
        form = FarmForm(request.POST, request.FILES, instance=farm)
        if form.is_valid():
            form.save()
            return redirect("farm_list")
    else:
        form = FarmForm(instance=farm)
    return render(request, "farms/farm_form.html", {"form": form})

def farm_delete(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    if request.method == "POST":
        farm.delete()
        return redirect("farm_list")
    return render(request, "farms/farm_confirm_delete.html", {"farm": farm})

from django.shortcuts import render
from django.db.models import Count
from farmers.models import Farmer
from farms.models import Farm

def dashboard_overview(request):
    total_farmers = Farmer.objects.count()
    total_farms = Farm.objects.count()

    # Crop distribution (count by primary_crop)
    crop_distribution = (
        Farm.objects.values("primary_crop__name")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    context = {
        "total_farmers": total_farmers,
        "total_farms": total_farms,
        "crop_distribution": crop_distribution,
        "farms": Farm.objects.select_related("farmer", "primary_crop"),
    }
    farms = Farm.objects.all()
    farm_data = [
        {"name": f.id, "lat": f.latitude, "lng": f.longitude}
        for f in farms
    ]

    context["farms"] = farm_data
    return render(request, "dashboard.html", context)
