/*
  Warnings:

  - You are about to drop the column `createdAt` on the `stock` table. All the data in the column will be lost.
  - You are about to drop the column `updateAt` on the `stock` table. All the data in the column will be lost.
  - You are about to alter the column `updated_at` on the `user` table. The data in that column could be lost. The data in that column will be cast from `DateTime(0)` to `DateTime`.

*/
-- AlterTable
ALTER TABLE `stock` DROP COLUMN `createdAt`,
    DROP COLUMN `updateAt`,
    ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NULL;

-- AlterTable
ALTER TABLE `user` MODIFY `updated_at` DATETIME NULL;
