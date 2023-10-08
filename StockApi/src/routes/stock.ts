import { FastifyInstance } from "fastify";
import { prisma } from "../lib/prisma";
import { z } from "zod";

export async function stockRoutes(fastify: FastifyInstance) {
    fastify.get('/stock', async () => {
        const stock = await prisma.stock.findMany()

        return { stock }
    })

    fastify.post('/stock', async (request, reply) => {
        const createStock = z.object({
            product_name: z.string(),
            product_price: z.number(),
            qnt_product: z.number(),
            FK_user_id: z.number(),
        })

        const { product_name, product_price, qnt_product, FK_user_id } = createStock.parse(request.body);

        await prisma.stock.create({
            data: {
                product_name,
                product_price,
                qnt_product,
                FK_user_id,
            }
        })

        return reply.status(201).send("Produto cadastrado com sucesso!")
    })

    fastify.put('/stock', async (request, reply) => {
        const createStock = z.object({
            stock_id: z.number(),
            product_name: z.string(),
            product_price: z.number(),
            qnt_product: z.number(),
            FK_user_id: z.number(),
        })

        const { stock_id, product_name, product_price, qnt_product, FK_user_id } = createStock.parse(request.body);

        let dataAtual = new Date();
        const dataFormatada = dataAtual.toISOString();

        await prisma.stock.update({
            where: {
                stock_id
            },
            data: {
                product_name,
                product_price,
                qnt_product,
                FK_user_id,
                updated_at: dataFormatada
            }
        })

        return reply.status(201).send("Produto atulizado com sucesso!")
    })

    fastify.delete<{ Params: { id: string } }>('/stock/:stock_id', async (request, reply) => {
        let { stock_id } = request.params;

        // Converte stock_id para um número inteiro
        stock_id = parseInt(stock_id);

        await prisma.stock.delete({
            where: {
                stock_id
            }
        });

        reply.status(204).send("Produto deletado com sucesso!");
    });
}