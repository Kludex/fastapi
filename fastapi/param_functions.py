from typing import Any, Callable, Optional, Sequence

from fastapi import params


def Path(  # noqa: N802
    default: Any,
    *,
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    deprecated: Optional[bool] = None,
    **extra: Any,
) -> Any:
    """[summary]

    Args:
        alias (Optional[str], optional): [description]. Defaults to None.
        title (Optional[str], optional): [description]. Defaults to None.
        description (Optional[str], optional): [description]. Defaults to None.
        gt (Optional[float], optional): [description]. Defaults to None.
        ge (Optional[float], optional): [description]. Defaults to None.
        lt (Optional[float], optional): [description]. Defaults to None.
        le (Optional[float], optional): [description]. Defaults to None.
        min_length (Optional[int], optional): [description]. Defaults to None.
        max_length (Optional[int], optional): [description]. Defaults to None.
        regex (Optional[str], optional): [description]. Defaults to None.
        deprecated (Optional[bool], optional): [description]. Defaults to None.

    Returns:
        Any: [description]
    """
    return params.Path(
        default=default,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        deprecated=deprecated,
        **extra,
    )


def Query(  # noqa: N802
    default: Any,
    *,
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    deprecated: Optional[bool] = None,
    **extra: Any,
) -> Any:
    """[summary]

    Args:
        alias (Optional[str], optional): [description]. Defaults to None.
        title (Optional[str], optional): [description]. Defaults to None.
        description (Optional[str], optional): [description]. Defaults to None.
        gt (Optional[float], optional): [description]. Defaults to None.
        ge (Optional[float], optional): [description]. Defaults to None.
        lt (Optional[float], optional): [description]. Defaults to None.
        le (Optional[float], optional): [description]. Defaults to None.
        min_length (Optional[int], optional): [description]. Defaults to None.
        max_length (Optional[int], optional): [description]. Defaults to None.
        regex (Optional[str], optional): [description]. Defaults to None.
        deprecated (Optional[bool], optional): [description]. Defaults to None.

    Returns:
        Any: [description]
    """
    return params.Query(
        default,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        deprecated=deprecated,
        **extra,
    )


def Header(  # noqa: N802
    default: Any,
    *,
    alias: Optional[str] = None,
    convert_underscores: bool = True,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    deprecated: Optional[bool] = None,
    **extra: Any,
) -> Any:
    """[summary]

    Args:
        alias (Optional[str], optional): [description]. Defaults to None.
        convert_underscores (bool, optional): [description]. Defaults to True.
        title (Optional[str], optional): [description]. Defaults to None.
        description (Optional[str], optional): [description]. Defaults to None.
        gt (Optional[float], optional): [description]. Defaults to None.
        ge (Optional[float], optional): [description]. Defaults to None.
        lt (Optional[float], optional): [description]. Defaults to None.
        le (Optional[float], optional): [description]. Defaults to None.
        min_length (Optional[int], optional): [description]. Defaults to None.
        max_length (Optional[int], optional): [description]. Defaults to None.
        regex (Optional[str], optional): [description]. Defaults to None.
        deprecated (Optional[bool], optional): [description]. Defaults to None.

    Returns:
        Any: [description]
    """
    return params.Header(
        default,
        alias=alias,
        convert_underscores=convert_underscores,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        deprecated=deprecated,
        **extra,
    )


def Cookie(  # noqa: N802
    default: Any,
    *,
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    deprecated: Optional[bool] = None,
    **extra: Any,
) -> Any:
    """[summary]

    Args:
        alias (Optional[str], optional): [description]. Defaults to None.
        title (Optional[str], optional): [description]. Defaults to None.
        description (Optional[str], optional): [description]. Defaults to None.
        gt (Optional[float], optional): [description]. Defaults to None.
        ge (Optional[float], optional): [description]. Defaults to None.
        lt (Optional[float], optional): [description]. Defaults to None.
        le (Optional[float], optional): [description]. Defaults to None.
        min_length (Optional[int], optional): [description]. Defaults to None.
        max_length (Optional[int], optional): [description]. Defaults to None.
        regex (Optional[str], optional): [description]. Defaults to None.
        deprecated (Optional[bool], optional): [description]. Defaults to None.

    Returns:
        Any: [description]
    """
    return params.Cookie(
        default,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        deprecated=deprecated,
        **extra,
    )


def Body(  # noqa: N802
    default: Any,
    *,
    embed: bool = False,
    media_type: str = "application/json",
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    **extra: Any,
) -> Any:
    """[summary]

    Args:
        embed (bool, optional): [description]. Defaults to False.
        media_type (str, optional): [description]. Defaults to "application/json".
        alias (Optional[str], optional): [description]. Defaults to None.
        title (Optional[str], optional): [description]. Defaults to None.
        description (Optional[str], optional): [description]. Defaults to None.
        gt (Optional[float], optional): [description]. Defaults to None.
        ge (Optional[float], optional): [description]. Defaults to None.
        lt (Optional[float], optional): [description]. Defaults to None.
        le (Optional[float], optional): [description]. Defaults to None.
        min_length (Optional[int], optional): [description]. Defaults to None.
        max_length (Optional[int], optional): [description]. Defaults to None.
        regex (Optional[str], optional): [description]. Defaults to None.

    Returns:
        Any: [description]
    """
    return params.Body(
        default,
        embed=embed,
        media_type=media_type,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        **extra,
    )


def Form(  # noqa: N802
    default: Any,
    *,
    media_type: str = "application/x-www-form-urlencoded",
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    **extra: Any,
) -> Any:
    """[summary]

    Args:
        media_type (str, optional): [description]. Defaults to "application/x-www-form-urlencoded".
        alias (Optional[str], optional): [description]. Defaults to None.
        title (Optional[str], optional): [description]. Defaults to None.
        description (Optional[str], optional): [description]. Defaults to None.
        gt (Optional[float], optional): [description]. Defaults to None.
        ge (Optional[float], optional): [description]. Defaults to None.
        lt (Optional[float], optional): [description]. Defaults to None.
        le (Optional[float], optional): [description]. Defaults to None.
        min_length (Optional[int], optional): [description]. Defaults to None.
        max_length (Optional[int], optional): [description]. Defaults to None.
        regex (Optional[str], optional): [description]. Defaults to None.

    Returns:
        Any: [description]
    """
    return params.Form(
        default,
        media_type=media_type,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        **extra,
    )


def File(  # noqa: N802
    default: Any,
    *,
    media_type: str = "multipart/form-data",
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    **extra: Any,
) -> Any:
    """[summary]

    Args:
        media_type (str, optional): [description]. Defaults to "multipart/form-data".
        alias (Optional[str], optional): [description]. Defaults to None.
        title (Optional[str], optional): [description]. Defaults to None.
        description (Optional[str], optional): [description]. Defaults to None.
        gt (Optional[float], optional): [description]. Defaults to None.
        ge (Optional[float], optional): [description]. Defaults to None.
        lt (Optional[float], optional): [description]. Defaults to None.
        le (Optional[float], optional): [description]. Defaults to None.
        min_length (Optional[int], optional): [description]. Defaults to None.
        max_length (Optional[int], optional): [description]. Defaults to None.
        regex (Optional[str], optional): [description]. Defaults to None.

    Returns:
        Any: [description]
    """
    return params.File(
        default,
        media_type=media_type,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        **extra,
    )


def Depends(  # noqa: N802
    dependency: Optional[Callable] = None, *, use_cache: bool = True
) -> Any:
    """[summary]

    Args:
        use_cache (bool, optional): [description]. Defaults to True.

    Returns:
        Any: [description]
    """
    return params.Depends(dependency=dependency, use_cache=use_cache)


def Security(  # noqa: N802
    dependency: Optional[Callable] = None,
    *,
    scopes: Optional[Sequence[str]] = None,
    use_cache: bool = True,
) -> Any:
    """[summary]

    Args:
        scopes (Optional[Sequence[str]], optional): [description]. Defaults to None.
        use_cache (bool, optional): [description]. Defaults to True.

    Returns:
        Any: [description]
    """
    return params.Security(dependency=dependency, scopes=scopes, use_cache=use_cache)
