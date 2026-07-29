# Test plan — varkasa

## Summary

Deep Regression Testing Plan for varkasa App

## Coverage

- **31** automated (`Run=Y`) · **12** manual (`Run=N`) · **43** plans in y1Plans.

## User stories

- **Login Flow Test** (automated) — Verify login functionality on home page
- **Search Functionality Test** (automated) — Test search bar functionality on products page
- **Product Details Page Test** (automated) — Verify product details page content and navigation
- **Cart Management Test** (automated) — Test cart management functionality on checkout page
- **Payment Gateway Integration Test** (automated) — Verify payment gateway integration with credit card
- **Admin Dashboard Test** (manual) — Verify admin dashboard functionality and navigation
- **User Profile Management Test** (automated) — Test user profile management functionality on account page
- **Order History Test** (automated) — Verify order history page content and filtering
- **Shipping Options Test** (automated) — Test shipping options selection on checkout page
- **Return Policy Test** (automated) — Verify return policy page content and navigation
- **FAQs Page Test** (automated) — Test FAQs page content and filtering
- **Settings Page Test** (manual) — Verify settings page functionality and navigation
- **Error Handling Test** (automated) — Test error handling on 404 page
- **Manual Mobile App Test** (manual) — Test manual mobile app functionality on iOS and Android
- **Manual UX Testing** (manual) — Test user experience on home page navigation
- **Manual UX Testing** (manual) — Test user experience on product details page navigation

## Test cases (BRAHL draft)

- `TC1` Verify login button functionality on home page [auto]
- `TC2` Test search bar input validation on products page [auto]
- `TC3` Verify product details page content and navigation [auto]
- `TC4` Test cart management functionality on checkout page [auto]
- `TC5` Verify payment gateway integration with credit card [auto]
- `TC6` Test admin dashboard login functionality [manual]
- `TC7` Verify user profile management functionality on account page [auto]
- `TC8` Test order history page content and filtering [auto]
- `TC9` Verify shipping options selection on checkout page [auto]
- `TC10` Test return policy page content and navigation [auto]
- `TC11` Verify FAQs page content and filtering [auto]
- `TC12` Test settings page functionality and navigation [manual]
- `TC13` Verify error handling on 404 page [auto]
- `TC14` Test manual mobile app installation on iOS device [manual]
- `TC15` Test user experience on home page navigation [manual]
- `TC16` Test user experience on product details page navigation [manual]
- `TC17` Test user experience on checkout page navigation [manual]
- `TC18` Test user experience on account page navigation [manual]
- `TC19` Verify product category filtering on products page [auto]
- `TC20` Test product image upload functionality [auto]
- `TC21` Verify product description input validation [auto]
- `TC22` Test product price update functionality [auto]
- `TC23` Verify product quantity reduction on cart page [auto]
- `TC24` Test product removal from cart functionality [auto]
- `TC25` Verify order status update on order history page [auto]
- `TC26` Test shipping rate calculation on checkout page [auto]
- `TC27` Verify payment method selection on checkout page [auto]
- `TC28` Test coupon code application on checkout page [auto]
- `TC29` Verify product availability on products page [auto]
- `TC30` Test product rating submission functionality [auto]

## yPAD plans (`y1Plans.csv`)

| PlanId | PlanName | Run | Tags |
| --- | --- | --- | --- |
| PReuse_Varkasa_OpenSite | Open browser and navigate to varkasa | N | Reuse |
| PVarkasa_T1_Test_case_1 | Test case 1 | Y | varkasa;Smoke;BRAHL;T1 |
| PVarkasa_T2_Test_case_2 | Test case 2 | Y | varkasa;Smoke;BRAHL;T2 |
| PVarkasa_T4_Test_case_4 | Test case 4 | Y | varkasa;Smoke;BRAHL;T4 |
| PVarkasa_T5_Test_case_5 | Test case 5 | Y | varkasa;Smoke;BRAHL;T5 |
| PVarkasa_T7_Test_case_7 | Test case 7 | Y | varkasa;Smoke;BRAHL;T7 |
| PVarkasa_T8_Test_case_8 | Test case 8 | Y | varkasa;Smoke;BRAHL;T8 |
| PVarkasa_T10_Test_case_10 | Test case 10 | Y | varkasa;Smoke;BRAHL;T10 |
| PVarkasa_T11_Test_case_11 | Test case 11 | Y | varkasa;Smoke;BRAHL;T11 |
| PVarkasa_Man_T3_Test_case_3 | Test case 3 | N | varkasa;Manual;T3 |
| PVarkasa_Man_T6_Test_case_6 | Test case 6 | N | varkasa;Manual;T6 |
| PVarkasa_Man_T9_Test_case_9 | Test case 9 | N | varkasa;Manual;T9 |
| PVarkasa_Man_T12_Test_case_12 | Test case 12 | N | varkasa;Manual;T12 |
| PVarkasa_TC1_Verify_login_button_func | Verify login button functionality on home page | Y | varkasa;Smoke;BRAHL;TC1 |
| PVarkasa_TC2_Test_search_bar_input_va | Test search bar input validation on products page | Y | varkasa;Smoke;BRAHL;TC2 |
| PVarkasa_TC3_Verify_product_details_p | Verify product details page content and navigation | Y | varkasa;Smoke;BRAHL;TC3 |
| PVarkasa_TC4_Test_cart_management_fun | Test cart management functionality on checkout page | Y | varkasa;Smoke;BRAHL;TC4 |
| PVarkasa_TC5_Verify_payment_gateway_i | Verify payment gateway integration with credit card | Y | varkasa;Smoke;BRAHL;TC5 |
| PVarkasa_TC7_Verify_user_profile_mana | Verify user profile management functionality on account page | Y | varkasa;Smoke;BRAHL;TC7 |
| PVarkasa_TC8_Test_order_history_page_ | Test order history page content and filtering | Y | varkasa;Smoke;BRAHL;TC8 |
| PVarkasa_TC9_Verify_shipping_options_ | Verify shipping options selection on checkout page | Y | varkasa;Smoke;BRAHL;TC9 |
| PVarkasa_TC10_Test_return_policy_page | Test return policy page content and navigation | Y | varkasa;Smoke;BRAHL;TC10 |
| PVarkasa_TC11_Verify_FAQs_page_conten | Verify FAQs page content and filtering | Y | varkasa;Smoke;BRAHL;TC11 |
| PVarkasa_TC13_Verify_error_handling_o | Verify error handling on 404 page | Y | varkasa;Smoke;BRAHL;TC13 |
| PVarkasa_TC19_Verify_product_category | Verify product category filtering on products page | Y | varkasa;Smoke;BRAHL;TC19 |
| PVarkasa_TC20_Test_product_image_uplo | Test product image upload functionality | Y | varkasa;Smoke;BRAHL;TC20 |
| PVarkasa_TC21_Verify_product_descript | Verify product description input validation | Y | varkasa;Smoke;BRAHL;TC21 |
| PVarkasa_TC22_Test_product_price_upda | Test product price update functionality | Y | varkasa;Smoke;BRAHL;TC22 |
| PVarkasa_TC23_Verify_product_quantity | Verify product quantity reduction on cart page | Y | varkasa;Smoke;BRAHL;TC23 |
| PVarkasa_TC24_Test_product_removal_fr | Test product removal from cart functionality | Y | varkasa;Smoke;BRAHL;TC24 |
| PVarkasa_TC25_Verify_order_status_upd | Verify order status update on order history page | Y | varkasa;Smoke;BRAHL;TC25 |
| PVarkasa_TC26_Test_shipping_rate_calc | Test shipping rate calculation on checkout page | Y | varkasa;Smoke;BRAHL;TC26 |
| PVarkasa_TC27_Verify_payment_method_s | Verify payment method selection on checkout page | Y | varkasa;Smoke;BRAHL;TC27 |
| PVarkasa_TC28_Test_coupon_code_applic | Test coupon code application on checkout page | Y | varkasa;Smoke;BRAHL;TC28 |
| PVarkasa_TC29_Verify_product_availabi | Verify product availability on products page | Y | varkasa;Smoke;BRAHL;TC29 |
| PVarkasa_TC30_Test_product_rating_sub | Test product rating submission functionality | Y | varkasa;Smoke;BRAHL;TC30 |
| PVarkasa_Man_TC6_Test_admin_dashboard_log | Test admin dashboard login functionality | N | varkasa;Manual;TC6 |
| PVarkasa_Man_TC12_Test_settings_page_func | Test settings page functionality and navigation | N | varkasa;Manual;TC12 |
| PVarkasa_Man_TC14_Test_manual_mobile_app_ | Test manual mobile app installation on iOS device | N | varkasa;Manual;TC14 |
| PVarkasa_Man_TC15_Test_user_experience_on | Test user experience on home page navigation | N | varkasa;Manual;TC15 |
| PVarkasa_Man_TC16_Test_user_experience_on | Test user experience on product details page navigation | N | varkasa;Manual;TC16 |
| PVarkasa_Man_TC17_Test_user_experience_on | Test user experience on checkout page navigation | N | varkasa;Manual;TC17 |
| PVarkasa_Man_TC18_Test_user_experience_on | Test user experience on account page navigation | N | varkasa;Manual;TC18 |

## How to run

Execute via FoXYiZ fEngine2 — low-code Tests/Steps/Test data CSVs. No Playwright.

_Source: `y/varkasa/test_plan.md` (synthesized if the file was missing)._