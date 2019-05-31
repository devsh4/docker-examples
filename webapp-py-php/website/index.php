<html>
  <head>
    <title>My Shop</title>
  </head>

  <body>
      <h1>Welcome to Dev's shop</h1>
      <ul>
          <?php
            $json = file_get_contents('http://product-service');
            $obj = json_decode($json);

            $products = $obj->products;
            echo "<div><b> Products offered: </b></div>";
            foreach ($products as $product) {
              echo "<li>$product</li>";
            }

            $json1 = file_get_contents('http://product-details-service');
            $obj1 = json_decode($json1);

            $productDetails = $obj1->productDetails;
            echo "<br><div><b> Product Details: </b></div>";
            foreach ($productDetails as $x) {
              echo "<li>$x</li>";
            }
          ?>
      </ul>
