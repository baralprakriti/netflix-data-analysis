CREATE TABLE `netflix_titles` (
  `show_id` text,
  `type` text,
  `title` text,
  `director` text,
  `cast` text,
  `country` text,
  `date_added` text,
  `release_year` bigint DEFAULT NULL,
  `rating` text,
  `duration` text,
  `listed_in` text,
  `description` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
