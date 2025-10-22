# Robot Test Cases for Saucedemo Website

## Test Cases

---

### TS 1: Login Test
**Steps:**
1. Open browser and go to [https://www.saucedemo.com/](https://www.saucedemo.com/)
2. Enter valid username and password
3. Click "Login" button
4. Verify that the user is redirected to the inventory page

---

### TS 2: Invalid Login Test
**Steps:**
1. Open browser and go to [https://www.saucedemo.com/](https://www.saucedemo.com/)
2. Enter invalid username and password
3. Click "Login" button
4. Verify that an error message is displayed

---

### TS 3: Add Product To Cart
**Steps:**
1. Log in with valid credentials
2. Click "Add to cart" on a product
3. Go to the cart page
4. Verify that the selected product is present in the cart

---

### TS 4: Remove Product From Cart
**Steps:**
1. Log in with valid credentials
2. Add a product to the cart
3. Navigate to the cart page
4. Click "Remove" button
5. Verify that the product is removed from the cart

---

### TS 5: Logout Test
**Steps:**
1. Log in with valid credentials
2. Click the menu button
3. Select "Logout" option
4. Verify that the login page is displayed again

---

### TS 6: Verify Product Sorting (Low → High)
**Steps:**
1. Log in with valid credentials
2. Open the product sort dropdown
3. Select "Price (low to high)"
4. Verify that all product prices are sorted correctly from lowest to highest

---

### TS 7: Add Multiple Products To Cart
**Steps:**
1. Log in with valid credentials
2. Add three different products to the cart
3. Verify that the cart badge shows "3"
4. Open the cart page
5. Verify that three products are listed

---

### TS 8: UI Elements Visibility Test
**Steps:**
1. Log in with valid credentials
2. Verify that the following elements are visible:
   - Website logo
   - Inventory list
   - Shopping cart icon
