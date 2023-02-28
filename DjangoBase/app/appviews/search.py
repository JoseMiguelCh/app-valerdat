from django.http import JsonResponse
from app.utils.wordfinder import WordFinder
from app.models import Product

class Search:
    def __init__(self) -> None:
        self.finder = None

    def word_finder(request, input_word) -> JsonResponse:
        """Find the longest word that can be made from the given letters.
        Args:
            request (HttpRequest): HTTP request. The input_word is passed as a GET parameter.
        Returns:
            JsonResponse: JSON response with the longest word that can be made from the given letters."""
        
        finder = WordFinder()
        longest = finder.longest_word(input_word)
        return JsonResponse({'longest_word': longest})

    def search_coords(request) -> JsonResponse:
        """Search for the product with the longest name that can be formed using the letters of the input product name.
        Args:
            request (HttpRequest): HTTP request. The product name is passed as a GET parameter.
        Returns:
            JsonResponse: JSON response with the product reference, name, volume and created date or error if the product isnt found. """
        
        product_name = request.GET.get('product')
        products = Product.objects.all()
        names: list[str] = [p.name.lower() for p in products]
        finder = WordFinder(names, type='internal')
        longest_prd = finder.longest_word(product_name)
        product = Product.objects.filter(name__iexact=longest_prd).first()

        if product:
            data = {'reference': product.reference, 'name': product.name, 'volume': product.volume, 'created': str(product.created)}
        else:
            data = {'error': f'No product found with longest name that can be formed using the letters of "{product_name}".'}
        return JsonResponse(data)