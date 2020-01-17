def paginate_queryset(query_set, page=1, per_page=10, return_list=True):
    """
    Paginate a query set (mongoengine.queryset.QuerySet)
    Args:
        page (int): Page number. Defaults to 1.
        per_page (int): Number of items per page. Defaults to 10.
        return_list (bool): Transform the query set into a list. Defaults to True.
    Returns:
        dict: A dict containing the result of the request.
    """
    offset = (page - 1) * per_page
    paginated_query = query_set.skip(offset).limit(per_page)
    return list(paginated_query) if return_list else paginated_query

def paginated_query(doc_class, query_params, page=1, per_page=10, show_total_count=True, envelope=None, show_page_info=True):
    """
    Perform a paginated query (mongoengine.queryset.QuerySet)
    Args:
        page (int): Page number. Defaults to 1.
        per_page (int): Number of items per page. Defaults to 10.
        show_total_count (bool): Return a ``total_count`` field in the response. Note that this may slow down the request.
            Defaults to True.
        envelope (bool): Envelope name containing the fetched items.
        show_page_info (bool): Show pagination info.
    Returns:
        dict: A dict containing the result of the request.
    """
    offset = (page - 1) * per_page
    paginated_query = doc_class.objects(
        **query_params).skip(offset).limit(per_page)
    docs = list(paginated_query)
    envelope = envelope if envelope else 'items'
    docs = {envelope: docs}
    count = {
        'count': len(docs[envelope])
    }
    page_info = {}
    if show_page_info:
        page_info['page'] = page
        page_info['per_page'] = per_page
    if show_total_count:
        count['total_count'] = doc_class.objects(**query_params).count()
    return {**count, **page_info, **docs}