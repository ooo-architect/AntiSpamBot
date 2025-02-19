from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot import messages
from bot.utils.chat_queries import get_chat_groups_dictionaries

router = Router()


@router.message(F.text == 'Активировать фильтр матов')
async def activate_profanity_filter(message: Message, state: FSMContext):
    await state.clear()

    chat_dicts = await get_chat_groups_dictionaries(message.chat.id)
    for dictionary in chat_dicts:
        dictionary.profanity_filter = True
        await dictionary.save()

    await message.answer(messages.SUCCESSFUL_ACTIVATE_FILTER)


@router.message(F.text == 'Выключить фильтр матов')
async def deactivate_profanity_filter(message: Message, state: FSMContext):
    await state.clear()

    chat_dicts = await get_chat_groups_dictionaries(message.chat.id)
    for dictionary in chat_dicts:
        dictionary.profanity_filter = False
        await dictionary.save()

    await message.answer(messages.SUCCESSFUL_DEACTIVATE_FILTER)
