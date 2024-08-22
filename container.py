#
# index = 1
#
# lol = {'<<': index - 1 , f'1/10 = index/len(categories[message.text].value)', '>>': index + 1}
#
#
#
#
#
# def anecdots_pagination(ind, st1=None):
#     dct = {'<<': 1, '>>': -1}
#     return ind - dct[st1]
#

#
# st1 = '1/1'
# st2 = '11'
# print(st1.count('/'), '--', st2.count('/'))


#
# from aiogram import Router
#
# dp = Dispatcher()
# router = Router
#
# dp.include_router("module_name".router)
#
#


##########################################################################################3

# # category selection
# @dis.message(IsCategory())
# async def anecdots(message: Message, state: FSMContext):
#     await message.answer(f'{categories_jokes_vip[message.text][1]}',
#                          reply_markup=reading_keyboard(index=1, count=len(categories_jokes_vip[message.text])).as_markup(resize_keyboard=True))
#     await state.update_data(index=1)
#     await state.update_data(category=message.text)
#     await state.update_data(count=len(categories_jokes[message.text]))
#     await state.update_data(count_vip=len(categories_jokes_vip[message.text]))
#     await state.set_state(fsm_reading.reading)
#
#     log.info(f'sending anecdots by category - {(await state.get_data())["category"]}')
#     log.info('entering a reading state')
#
#
# # entering reading state
# # vip user filter realize here
# @dis.message(StateFilter(fsm_reading.reading), lambda x: x.text != 'Back')
# async def reading_state(message: Message, state: FSMContext):
#     try:
#         # VIP USER
#         if IsVipUser_func(message):
#             print('VIP')
#             if not message.text.count('/'):
#                 dct_moves = {'<<': 1, '>>': -1}
#                 if ((await state.get_data())['index'] - dct_moves[message.text]) <= 0:
#                     await message.answer('Назад? только вперед!',
#                                          reply_markup=reading_keyboard(index=(await state.get_data())['index'],
#                                                                        count=(await state.get_data())['count_vip']).as_markup(resize_keyboard=True))
#                     log.debug('error limits - protect')
#                 elif ((await state.get_data())['index'] - dct_moves[message.text]) >= (await state.get_data())['count_vip']:
#                     await message.answer(
#                         'а больше нету',
#                         reply_markup=reading_keyboard(index=(await state.get_data())['index'],
#                                                       count=(await state.get_data())['count_vip']).as_markup(resize_keyboard=True))
#                     log.debug('limits - protect')
#                 else:
#                     await state.update_data(index=(await state.get_data())['index'] - dct_moves[message.text])
#                     await message.answer(
#                         categories_jokes_vip[(await state.get_data())['category']][(await state.get_data())['index']],
#                         reply_markup=reading_keyboard(index=(await state.get_data())['index'],
#                                                       count=(await state.get_data())['count_vip']).as_markup(resize_keyboard=True))
#                     log.info(f'sending anecdot by new index - {(await state.get_data())["index"]}')
#             else:
#                 await message.answer((await state.get_data())['category'],
#                                      reply_markup=numbers_category_jokes_vip((await state.get_data())['category']).as_markup())
#                 log.info('sending keyboard with anecdots')
#
#         else:
#             # NOT VIP USER
#             print('NOT VIP')
#             if not message.text.count('/'):
#                 dct_moves = {'<<': 1, '>>': -1}
#                 if ((await state.get_data())['index'] - dct_moves[message.text]) <= 0:
#                     await message.answer('Назад? только вперед!', reply_markup=reading_keyboard(index=(await state.get_data())['index'],
#                                                                         count=(await state.get_data())['count_vip']).as_markup(resize_keyboard=True))
#                     log.debug('error limits - protect')
#                 elif ((await state.get_data())['index'] - dct_moves[message.text]) >= (int((await state.get_data())['count_vip']) // 2):
#                     await message.answer('Что бы смотреть больше анекдотов и больше категорий,\nжми- /vip  и покупай по скидке',
#                                          reply_markup=reading_keyboard(index=(await state.get_data())['index'],
#                                                                        count=(await state.get_data())['count_vip']).as_markup(resize_keyboard=True))
#                     log.debug('no vip user - protect')
#                 else:
#                     await state.update_data(index=(await state.get_data())['index'] - dct_moves[message.text])
#                     await message.answer(categories_jokes[(await state.get_data())['category']][(await state.get_data())['index']],
#                                          reply_markup=reading_keyboard(index=(await state.get_data())['index'],
#                                                                        count=(await state.get_data())['count_vip']).as_markup(resize_keyboard=True))
#                     log.info(f'sending anecdot by new index - {(await state.get_data())["index"]}')
#             else:
#                 await message.answer((await state.get_data())['category'], reply_markup=numbers_category_jokes((await state.get_data())['category']).as_markup())
#                 log.info('sending keyboard with anecdots')
#
#     except KeyError:
#         await message.answer('Для перехода к другому анекдоту нужно нажать кнопку снизу')
#
#
#
#
# @dis.message(StateFilter(fsm_reading.reading), lambda x: x.text == 'Back')
# async def reading_state_cancel(message: Message, state: FSMContext, bot: Bot):
#     await state.clear()
#     log.info('exit a reading state')
#     await message.answer('You go to categories', reply_markup=jc_keyboard)
#
#
#
#
# @dis.callback_query(StateFilter(fsm_reading.reading))
# async def reading_state_callback_answer(callback: CallbackQuery, state: FSMContext):
#     if callback.data.split('-')[1] == (await state.get_data())['category']:
#         ind = int(callback.data.split('-')[0])
#         # if IsVipUser_func(callback.message):
#         await state.update_data(index=ind)
#         await state.update_data(user_message_id={callback.from_user.id: callback.inline_message_id})
#         await callback.message.answer(categories_jokes[(await state.get_data())['category']][ind],
#                                       reply_markup=reading_keyboard(index=ind, count=(await state.get_data())['count_vip']).as_markup(resize_keyboard=True))
#         #     await callback.message.answer('VIP')
#         # else:
#         #     await callback.message.answer('VIP')
#         #     await state.update_data(index=ind)
#         #     await state.update_data(user_message_id={callback.from_user.id: callback.inline_message_id})
#         #     await callback.message.answer(categories_jokes[(await state.get_data())['category']][ind],
#         #                                   reply_markup=reading_keyboard(index=ind, count=(await state.get_data())['count_vip']).as_markup(resize_keyboard=True))
#
#         log.info(f'callback is handled, index - {(await state.get_data())["index"]}')
#     else:
#         await callback.message.answer('Воспользуйтесь кнопками что ниже')
#         log.debug(f'wrong inline keyboard - protected')



##########################################################################################3


# for k, v in dct.keys():
#     if k = old_cat_name:
#         k = new_cat_name
#
#
# dct = {1: [1, 2, 3], 2: [11, 2, 3], 3: [111, 2, 3]}
#
#
# dct.keys() = [2,3,4]
#
# print(dct)
#
# print(list(dct))
#
#




# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# # change category state, change category name
# @rout_admin.message(StateFilter(Admin.chng_cat), F.text)
# async def change_name(message: Message, state: FSMContext):
#     level = (await state.get_data())['chng_cat_level']
#     old_cat_name = (await state.get_data())['chng_cat_old_name']
#     new_cat_name = message.text
#     # global vip_lst_cats, vip_cat_jokes, vip_cat_jokes_key, \
#     #        usual_lst_cats, usual_cat_jokes, usual_cat_jokes_key
#     # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     cat_dct = {'VIP': [vip_lst_cats, vip_cat_jokes, vip_cat_jokes_key],
#                'USUAL': [usual_lst_cats, usual_cat_jokes, usual_cat_jokes_key]}
#
#     cat_dct[level][1] = dct_rename(cat_dct[level][1], old_cat_name, new_cat_name)
#     cat_dct[level][0] = list(cat_dct[level][1].keys())
#     # print(cat_dct[level][1], cat_dct[level][0])
#     # print(usual_lst_cats, usual_cat_jokes)
#     await message.answer(f'{old_cat_name} -> {new_cat_name}\n/back чтобы вернуться и поменять данные',
#                          reply_markup=cat_dct[level][2]().as_markup(resize_keyboard=True))
#     await message.answer(f'что то еще?',
#                          reply_markup=admin_actions().as_markup(resize_keyboard=True,
#                                                                 input_field_placeholder='клавиатура обновлена'))
#     await state.set_state(Admin.selection_state)
#     log.info(f'del_cat succes, set state selection state')









