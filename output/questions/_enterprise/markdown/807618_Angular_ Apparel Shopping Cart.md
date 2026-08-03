# Angular: Apparel Shopping Cart

## Metadata

- **ID:** 807618
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Angular, State Management, Event Binding, Data Binding, Easy, Theme:  E-commerce, TypeScript
- **Skills:** Angular (Basic)

## Summary

This front-end development question evaluates Angular, state management, and event binding concepts, ideal for junior-level roles. The problem requires implementing cart state functionality in ShoppingCartService to synchronize product catalog and cart line items.

## Problem Statement

You are given a fully designed Angular apparel shopping cart. It lets users browse a product catalog, add items to the cart, and adjust quantities per product row while the cart panel shows line items and totals. The app already has a polished layout, cards, and styling; your job is to implement the cart state in ShoppingCartService and keep the catalog rows and cart lines in sync.

      
      Hide preview Show preview

      
    

    
Your task is to implement the underlying functionality so that all the given test cases pass successfully.

    
      
- Implement ShoppingCartService.addLine and ShoppingCartService.updateLine so that adding or changing quantities updates the cart line items and each product's cartQuantity consistently.
      
- When quantity reaches zero, remove the cart line and restore the add-to-cart control on that product row.
      
- Ensure CartComponent computes totalQuantity as the sum of line quantities (zero for an empty cart).
      
- Keep ProductListComponent emitting onAddToCart and onQuantityUpdate with the updated product objects expected by the tests.
    

    
Note: Refer to the README.md file for detailed implementation requirements.

## Preview

You are given a fully designed Angular apparel shopping cart. It lets us
