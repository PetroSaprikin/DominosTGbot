def product_resolve_result(table, product_name):
    for product in table.select():
        if product.product_name == product_name:
            answer = f"Назва продукту: {product.product_name}\n" \
                    f"Зберігання закритої упаковки(з дати виробництва): {product.cooler}\n" \
                    f"Розморозка(годин) t = 1-3 *C: {product.defrost}\n" \
                    f"Відкрита упаковка(кіл-ть днів/годин в кулері/сухому складі): {product.opened}\n" \
                    f"Підготовлена продукція, кіл-ть днів при 1-5 *C градусах в меклайні: {product.prepared_make_line}\n" \
                    f"Підготовлена продукція(кіл-ть днів/годин) при 10-32 *C градусах: {product.prepared_owen}"
            return answer
