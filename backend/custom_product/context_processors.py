# from .models import CustomCategory, CustomProduct

# def menu_links(request):
#     # Fetch all categories
#     categories = CustomCategory.objects.all()
#     print("Categories fetched:", categories)  # Debug statement

#     # Create a list to store categories with their product counts
#     categories_with_counts = []

#     for category in categories:
#         # Count the number of products in this category
#         product_count = CustomProduct.objects.filter(categories=category).count()
#         print(f"Category: {category.name}, Product Count: {product_count}")  # Debug statement

#         # Append the category and its product count to the list
#         categories_with_counts.append({
#             'category': category,
#             'product_count': product_count,
#         })

#     # Debug the final output
#     print("Categories with counts:", categories_with_counts)

#     # Return the context
#     return {
#         'links': categories,
#         'categories_with_counts': categories_with_counts,
#     }