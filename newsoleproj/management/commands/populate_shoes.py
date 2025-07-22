from django.core.management.base import BaseCommand
from newsoleapp.models import Shoe

class Command(BaseCommand):
    help = 'Populate the Shoe model with 20 sample shoes using MultiSelectField for categories.'

    def handle(self, *args, **options):
        shoes_data = [
            {
                "name": "AirMax Runner",
                "description": "Lightweight running shoes with breathable mesh.",
                "image": "https://images.unsplash.com/photo-1517260911205-8eec7e1f1b6f?auto=format&fit=crop&w=500&q=80",
                "price": 99.99,
                "categories": ["POPULAR", "TRENDING"],
            },
            {
                "name": "Urban Classic",
                "description": "Classic sneakers for everyday wear.",
                "image": "https://images.unsplash.com/photo-1528701800484-905a6bafd3d6?auto=format&fit=crop&w=500&q=80",
                "price": 89.99,
                "categories": ["CLASSIC", "SALE"],
            },
            {
                "name": "Street Style",
                "description": "Trendy shoes with bold patterns.",
                "image": "https://images.unsplash.com/photo-1519864600265-abb23847ef2c?auto=format&fit=crop&w=500&q=80",
                "price": 110.00,
                "categories": ["TRENDING", "NEW"],
            },
            {
                "name": "Peak Performance",
                "description": "Shoes designed for high performance sports.",
                "image": "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=500&q=80",
                "price": 120.50,
                "categories": ["POPULAR", "NEW"],
            },
            {
                "name": "Retro Vibe",
                "description": "Old-school sneakers with a modern twist.",
                "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=500&q=80",
                "price": 79.99,
                "categories": ["CLASSIC", "SALE"],
            },
            {
                "name": "Hiking Pro",
                "description": "Rugged shoes for all your hiking adventures.",
                "image": "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=500&q=80",
                "price": 130.00,
                "categories": ["NEW", "POPULAR"],
            },
            {
                "name": "Sleek Black",
                "description": "Minimalist black shoes for any occasion.",
                "image": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?auto=format&fit=crop&w=500&q=80",
                "price": 95.00,
                "categories": ["TRENDING", "CLASSIC"],
            },
            {
                "name": "White Walker",
                "description": "Crisp white sneakers for a clean look.",
                "image": "https://images.unsplash.com/photo-1503341455253-b2e723bb3dbb?auto=format&fit=crop&w=500&q=80",
                "price": 105.00,
                "categories": ["POPULAR", "SALE"],
            },
            {
                "name": "Blue Chill",
                "description": "Cool blue shoes for a casual day out.",
                "image": "https://images.unsplash.com/photo-1512499617640-c2f999098c65?auto=format&fit=crop&w=500&q=80",
                "price": 88.88,
                "categories": ["TRENDING", "NEW"],
            },
            {
                "name": "Summer Breeze",
                "description": "Light and airy shoes for summer fun.",
                "image": "https://images.unsplash.com/photo-1465101178521-c1a9136a86d4?auto=format&fit=crop&w=500&q=80",
                "price": 70.00,
                "categories": ["SALE", "NEW"],
            },
            {
                "name": "Winter Guard",
                "description": "Warm shoes to keep your feet cozy in winter.",
                "image": "https://images.unsplash.com/photo-1434056886845-dac89ffe9b56?auto=format&fit=crop&w=500&q=80",
                "price": 140.00,
                "categories": ["POPULAR", "TRENDING"],
            },
            {
                "name": "Canvas Beat",
                "description": "Everyday canvas shoes with a beat.",
                "image": "https://images.unsplash.com/photo-1475189778702-5ec9941484ae?auto=format&fit=crop&w=500&q=80",
                "price": 60.00,
                "categories": ["CLASSIC", "SALE"],
            },
            {
                "name": "Energy Boost",
                "description": "Shoes that give you an extra bounce.",
                "image": "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=500&q=80",
                "price": 125.00,
                "categories": ["POPULAR", "NEW"],
            },
            {
                "name": "Leather Luxe",
                "description": "Premium leather shoes for style and comfort.",
                "image": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?auto=format&fit=crop&w=500&q=80",
                "price": 155.00,
                "categories": ["CLASSIC", "SALE"],
            },
            {
                "name": "Red Racer",
                "description": "Bold red shoes for those who love speed.",
                "image": "https://images.unsplash.com/photo-1517260911205-8eec7e1f1b6f?auto=format&fit=crop&w=500&q=80",
                "price": 99.99,
                "categories": ["TRENDING", "POPULAR"],
            },
            {
                "name": "Eco Step",
                "description": "Eco-friendly shoes made from recycled materials.",
                "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=500&q=80",
                "price": 85.00,
                "categories": ["NEW", "SALE"],
            },
            {
                "name": "Sport Lite",
                "description": "Lightweight sports shoes for all activities.",
                "image": "https://images.unsplash.com/photo-1512499617640-c2f999098c65?auto=format&fit=crop&w=500&q=80",
                "price": 112.00,
                "categories": ["POPULAR", "NEW"],
            },
            {
                "name": "Flex Fit",
                "description": "Shoes that flex to your every move.",
                "image": "https://images.unsplash.com/photo-1519864600265-abb23847ef2c?auto=format&fit=crop&w=500&q=80",
                "price": 102.50,
                "categories": ["TRENDING", "CLASSIC"],
            },
            {
                "name": "Mountain Trek",
                "description": "Durable shoes for mountain adventures.",
                "image": "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=500&q=80",
                "price": 138.00,
                "categories": ["NEW", "POPULAR"],
            },
            {
                "name": "Desert Tan",
                "description": "Stylish tan shoes for any casual outfit.",
                "image": "https://images.unsplash.com/photo-1465101178521-c1a9136a86d4?auto=format&fit=crop&w=500&q=80",
                "price": 90.00,
                "categories": ["SALE", "CLASSIC"],
            },
        ]

        count = 0
        for data in shoes_data:
            shoe, created = Shoe.objects.get_or_create(
                name=data["name"],
                defaults={
                    "description": data["description"],
                    "image": data["image"],
                    "price": data["price"],
                    "categories": data["categories"],
                }
            )
            if created:
                count += 1

        self.stdout.write(self.style.SUCCESS(f"{count} shoe products created successfully!"))