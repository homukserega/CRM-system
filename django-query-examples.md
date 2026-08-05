# Get all contracts with their products (eager loading)

    # Get all contracts with product data prefetched
    contracts = Contract.objects.select_related('product').all()

    # Access product data
    for contract in contracts:
        print(f"Contract: {contract.name}")
        print(f"Product: {contract.product}")  # Assuming product has __str__ method
        print(f"Product ID: {contract.product.id}")
    
# Filter contracts by specific product

    # Get all contracts for a specific product (assuming product_id exists)
    product_id = 1
    contracts = Contract.objects.filter(product_id=product_id)
    
    # Or filter by product attribute
    contracts = Contract.objects.filter(product__name="Some Product Name")
# Get all products that have contracts (distinct)

    # Get distinct products that have at least one contract
    from django.db.models import Count
    
    products_with_contracts = Contract.objects.values('product').distinct()
    
    # Or get products with contract count
    products_with_counts = Contract.objects.values('product').annotate(
        contract_count=Count('id')
    )

# Get contracts with product and related data

    # Get contracts with product data and filter by dates
    contracts = Contract.objects.select_related('product').filter(
        start_date__gte=datetime.now(),
        end_date__isnull=True
    )
# If you need product details in the queryset

    # Assuming BASE_PRODUCT_MODEL has fields like 'name', 'price', etc.
    contracts = Contract.objects.select_related('product').all().values(
        'id',
        'name',
        'product__id',
        'product__name',  # Access product fields
        'product__price',
        'start_date',
        'end_date',
        'cost'
    )

# Example with full queryset

    from django.db.models import Q, F
    from datetime import datetime
    
    # Complex queryset getting contracts with product information
    contracts = (
        Contract.objects
        .select_related('product')
        .filter(
            Q(start_date__lte=datetime.now()) & 
            (Q(end_date__isnull=True) | Q(end_date__gte=datetime.now()))
        )
        .annotate(
            product_name=F('product__name'),  # Assuming product has 'name' field
            product_price=F('product__price')  # Assuming product has 'price' field
        )
        .order_by('-uploaded_at')
    )

    # Access the data
    for contract in contracts:
        print(f"Contract: {contract.name}")
        print(f"Product: {contract.product_name}")
        print(f"Product price: {contract.product_price}")
        print(f"Contract cost: {contract.cost}")

## Important Notes:

<i>The relationship is on the Contract side (ForeignKey), so each contract points to one product, but one product can have many contracts (One-to-Many).

The queryset structure when you access contract.product will return the product object (or model instance) based on your BASE_PRODUCT_MODEL settings.

To optimize queries, always use .select_related() when you know you'll access the product data, as it performs a JOIN and reduces database queries.</i>