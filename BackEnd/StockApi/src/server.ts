import Fastify from "fastify";
import cors from "@fastify/cors"
import { PrismaClient } from "@prisma/client";
import { stockRoutes } from "./routes/stock";

const prisma = new PrismaClient({
    log: ['query'],
})


async function bootstrap() {
    const fastify = Fastify({
        logger: true,
    })

    await fastify.register(cors, {
        origin: true,
    })

    await fastify.register(stockRoutes)

    await fastify.listen({ port: 3334, host: '0.0.0.0' });
}

bootstrap();