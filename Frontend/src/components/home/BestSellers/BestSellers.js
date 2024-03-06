import React, { useState, useEffect } from "react";
import axios from "axios";
import Heading from "../Products/Heading";
import Product from "../Products/Product";

const BestSellers = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchBestSellers = async () => {
      try {
        const response = await axios.get("http://localhost:8000/api/products/");
        setProducts(response.data);
      } catch (error) {
        console.error("Error fetching best sellers:", error);
      }
    };

    fetchBestSellers();
  }, []);

  return (
    <div className="w-full pb-20">
      <Heading heading="Our Bestsellers" />
      <div className="w-full grid grid-cols-1 md:grid-cols-2 lgl:grid-cols-3 xl:grid-cols-4 gap-10">
        {products.map((product) => (
          <Product
            key={product.id}
            _id={product.id}
            img={product.thumbnail} // Assuming your Django API returns the image URL in the 'img' field
            productName={product.title} // Assuming your Django API returns the product name in the 'productName' field
            price={product.price} // Assuming your Django API returns the price in the 'price' field
            des={product.description} // Assuming your Django API returns the description in the 'des' field
          />
        ))}
      </div>
    </div>
  );
};

export default BestSellers;
