import os

# Check CPU flags. This must be done before importing the Polars Rust bindings.
import polars._cpu_check

polars._cpu_check.check_cpu_flags()

try:
    # Ensure the object constructor is known by Polars.
    # We set this once on import

    # We also set other function pointers needed on the Rust side.
    # This function is highly unsafe and should only be called once.
    from polars.polars import __register_startup_deps

    __register_startup_deps()
except ImportError:  # Module not available when building docs
    pass

import polars._utils.polars_version
from polars import api, exceptions, plugins, selectors

# TODO: remove need for importing wrap utils at top level
from polars._utils.wrap import wrap_df, wrap_s  # noqa: F401
from polars.config import Config
from polars.convert import (
    from_arrow,
    from_dataframe,
    from_dict,
    from_dicts,
    from_numpy,
    from_pandas,
    from_records,
    from_repr,
    json_normalize,
)
from polars.dataframe import DataFrame
from polars.datatypes import (
    Array,
    Binary,
    Boolean,
    Categorical,
    DataType,
    Date,
    Datetime,
    Decimal,
    Duration,
    Enum,
    Field,
    Float32,
    Float64,
    Int8,
    Int16,
    Int32,
    Int64,
    List,
    Null,
    Object,
    String,
    Struct,
    Time,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
    Unknown,
    Utf8,
)
from polars.expr import Expr
from polars.functions import (
    align_frames,
    all,
    all_horizontal,
    any,
    any_horizontal,
    approx_n_unique,
    arange,
    arctan2,
    arctan2d,
    arg_sort_by,
    arg_where,
    business_day_count,
    coalesce,
    col,
    collect_all,
    collect_all_async,
    concat,
    concat_list,
    concat_str,
    corr,
    count,
    cov,
    cum_count,
    cum_fold,
    cum_reduce,
    cum_sum,
    cum_sum_horizontal,
    date,
    date_range,
    date_ranges,
    datetime,
    datetime_range,
    datetime_ranges,
    duration,
    element,
    exclude,
    field,
    first,
    fold,
    format,
    from_epoch,
    groups,
    head,
    implode,
    int_range,
    int_ranges,
    last,
    len,
    lit,
    map_batches,
    map_groups,
    max,
    max_horizontal,
    mean,
    mean_horizontal,
    median,
    min,
    min_horizontal,
    n_unique,
    nth,
    ones,
    quantile,
    reduce,
    repeat,
    rolling_corr,
    rolling_cov,
    select,
    set_random_seed,
    sql_expr,
    std,
    struct,
    sum,
    sum_horizontal,
    tail,
    time,
    time_range,
    time_ranges,
    var,
    when,
    zeros,
)
from polars.io import (
    read_avro,
    read_clipboard,
    read_csv,
    read_csv_batched,
    read_database,
    read_database_uri,
    read_delta,
    read_excel,
    read_ipc,
    read_ipc_schema,
    read_ipc_stream,
    read_json,
    read_ndjson,
    read_ods,
    read_parquet,
    read_parquet_schema,
    scan_csv,
    scan_delta,
    scan_iceberg,
    scan_ipc,
    scan_ndjson,
    scan_parquet,
    scan_pyarrow_dataset,
)
from polars.lazyframe import InProcessQuery, LazyFrame
from polars.meta import (
    build_info,
    get_index_type,
    show_versions,
    thread_pool_size,
    threadpool_size,
)
from polars.schema import Schema
from polars.series import Series
from polars.sql import SQLContext, sql
from polars.string_cache import (
    StringCache,
    disable_string_cache,
    enable_string_cache,
    using_string_cache,
)

__version__: str = polars._utils.polars_version._get_polars_version()

__all__ = [
    # modules
    "api",
    "exceptions",
    "plugins",
    "selectors",
    # core classes
    "DataFrame",
    "Expr",
    "LazyFrame",
    "Series",
    # other classes
    "InProcessQuery",
    "Schema",
    # polars.datatypes
    "Array",
    "Binary",
    "Boolean",
    "Categorical",
    "DataType",
    "Date",
    "Datetime",
    "Decimal",
    "Duration",
    "Enum",
    "Field",
    "Float32",
    "Float64",
    "Int8",
    "Int16",
    "Int32",
    "Int64",
    "List",
    "Null",
    "Object",
    "String",
    "Struct",
    "Time",
    "UInt8",
    "UInt16",
    "UInt32",
    "UInt64",
    "Unknown",
    "Utf8",
    # polars.io
    "read_avro",
    "read_clipboard",
    "read_csv",
    "read_csv_batched",
    "read_database",
    "read_database_uri",
    "read_delta",
    "read_excel",
    "read_ipc",
    "read_ipc_schema",
    "read_ipc_stream",
    "read_json",
    "read_ndjson",
    "read_ods",
    "read_parquet",
    "read_parquet_schema",
    "scan_csv",
    "scan_delta",
    "scan_iceberg",
    "scan_ipc",
    "scan_ndjson",
    "scan_parquet",
    "scan_pyarrow_dataset",
    # polars.stringcache
    "StringCache",
    "disable_string_cache",
    "enable_string_cache",
    "using_string_cache",
    # polars.config
    "Config",
    # polars.functions.whenthen
    "when",
    # polars.functions
    "align_frames",
    "arg_where",
    "business_day_count",
    "concat",
    "date_range",
    "date_ranges",
    "datetime_range",
    "datetime_ranges",
    "element",
    "ones",
    "repeat",
    "time_range",
    "time_ranges",
    "zeros",
    # polars.functions.aggregation
    "all",
    "all_horizontal",
    "any",
    "any_horizontal",
    "cum_sum",
    "cum_sum_horizontal",
    "max",
    "max_horizontal",
    "mean_horizontal",
    "min",
    "min_horizontal",
    "sum",
    "sum_horizontal",
    # polars.functions.lazy
    "approx_n_unique",
    "arange",
    "arctan2",
    "arctan2d",
    "arg_sort_by",
    "coalesce",
    "col",
    "collect_all",
    "collect_all_async",
    "concat_list",
    "concat_str",
    "corr",
    "count",
    "cov",
    "cum_count",
    "cum_fold",
    "cum_reduce",
    "cumfold",
    "cumreduce",
    "date",
    "datetime",
    "duration",
    "exclude",
    "field",
    "first",
    "fold",
    "format",
    "from_epoch",
    "groups",
    "head",
    "implode",
    "int_range",
    "int_ranges",
    "last",
    "lit",
    "map_batches",
    "map_groups",
    "mean",
    "median",
    "n_unique",
    "nth",
    "quantile",
    "reduce",
    "rolling_corr",
    "rolling_cov",
    "select",
    "std",
    "struct",
    "tail",
    "time",
    "var",
    # polars.functions.len
    "len",
    # polars.functions.random
    "set_random_seed",
    # polars.convert
    "from_arrow",
    "from_dataframe",
    "from_dict",
    "from_dicts",
    "from_numpy",
    "from_pandas",
    "from_records",
    "from_repr",
    "json_normalize",
    # polars.meta
    "build_info",
    "get_index_type",
    "show_versions",
    "thread_pool_size",
    "threadpool_size",
    # polars.sql
    "SQLContext",
    "sql",
    "sql_expr",
]

os.environ["POLARS_ALLOW_EXTENSION"] = "true"


def __getattr__(name: str):  # type: ignore[no-untyped-def]
    # Deprecate re-export of exceptions at top-level
    if name in dir(exceptions):
        from polars._utils.deprecation import issue_deprecation_warning

        issue_deprecation_warning(
            message=(
                f"Accessing `{name}` from the top-level `polars` module is deprecated."
                " Import it directly from the `polars.exceptions` module instead:"
                f" from polars.exceptions import {name}"
            ),
            version="1.0.0",
        )
        return getattr(exceptions, name)

    # Deprecate data type groups at top-level
    import polars.datatypes.group as dtgroup

    if name in dir(dtgroup):
        from polars._utils.deprecation import issue_deprecation_warning

        issue_deprecation_warning(
            message=(
                f"`{name}` is deprecated. Define your own data type groups or use the"
                " `polars.selectors` module for selecting columns of a certain data type."
            ),
            version="1.0.0",
        )
        return getattr(dtgroup, name)

    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)


# Remove symbols imported for internal use
del os
