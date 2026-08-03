# Spring MVC RestController

## Metadata

- **ID:** 1290392
- **Type:** multiple_mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Spring, Spring Boot, Medium
- **Skills:** Spring Boot (Intermediate)

## Summary

This multiple choice question evaluates Spring Boot, RESTful services, and controller methods concepts, ideal for mid-level roles. The problem requires identifying the correctness of statements regarding a specific controller method in a Spring Boot application.

## Problem Statement

`@RestController
@RequestMapping("/api/product/categories")
public class ProductCategoryController{
    @Autowired
    private CategorySerice categoryService;

    @GetMapping("/{id}/{locale}")
    public ResponseEntity<CategoryDto> getByIdAndLocale(@PathVariable("id") Long id,
                                                        @PathVariable("locale") String locale {
        CategoryDto dto = categoryService.getByIdAndLocale(id, locale);
        return new ResponseEntity<>(dto, HttpStatus.OK);
    }
}
`
```

Which of the following options are true about the given controller method?

## Preview

@RestController
